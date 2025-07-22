from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from jobs.models import Job, Application, SavedJob, LikedJob, DislikedJob
from profiles.models import User, CompanyFollows
from elasticsearch_dsl import analyzer, tokenizer

# Job Index
edge_ngram_analyzer = analyzer(
    'edge_ngram_analyzer',
    tokenizer=tokenizer(
        'edge_ngram_tokenizer',
        'edge_ngram',
        min_gram=1,
        max_gram=20,
        token_chars=["letter", "digit"]
    ),
    filter=["lowercase"]
)
@registry.register_document
class JobDocument(Document):
    company = fields.ObjectField(properties={
    'company_name': fields.TextField(analyzer=edge_ngram_analyzer, search_analyzer='standard'),})
    title = fields.TextField(analyzer=edge_ngram_analyzer, search_analyzer='standard')
    description = fields.TextField(analyzer=edge_ngram_analyzer, search_analyzer='standard')
    location = fields.TextField(analyzer=edge_ngram_analyzer, search_analyzer='standard')

    class Index:
        name = 'jobs'

    class Django:
        model = Job
        fields = [
            'job_id',
            'salary',
            'posted_at',
            'is_active',
        ]


# User Interaction Index
user_interactions_index = Index('user_interactions')
#user_interactions_index.settings(number_of_shards=1, number_of_replicas=0)

@registry.register_document
class UserInteractionDocument(Document):
    applied_jobs = fields.ListField(fields.KeywordField())
    saved_jobs = fields.ListField(fields.KeywordField())
    liked_jobs = fields.ListField(fields.KeywordField())
    disliked_jobs = fields.ListField(fields.KeywordField())
    followed_companies = fields.ListField(fields.KeywordField())

    class Index:
        name = 'user_interactions'

    class Django:
        model = User
        fields = ['user_id', 'username']

    def prepare_applied_jobs(self, instance):
        return list(Application.objects.filter(user=instance).values_list('job__job_id', flat=True))

    def prepare_saved_jobs(self, instance):
        return list(SavedJob.objects.filter(user=instance).values_list('job__job_id', flat=True))

    def prepare_liked_jobs(self, instance):
        return list(LikedJob.objects.filter(user=instance).values_list('job__job_id', flat=True))

    def prepare_disliked_jobs(self, instance):
        return list(DislikedJob.objects.filter(user=instance).values_list('job__job_id', flat=True))

    def prepare_followed_companies(self, instance):
        return list(CompanyFollows.objects.filter(user=instance).values_list('company__company_id', flat=True))
