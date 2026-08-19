import os
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from tracker.models import JobApplication, Interview, JobAnalysis, Category

def seed():
    print("[*] Clearing all existing database records for a fresh start...")
    # Delete in order of dependent models to ensure clean slate
    JobAnalysis.objects.all().delete()
    Interview.objects.all().delete()
    JobApplication.objects.all().delete()
    Category.objects.all().delete()
    User.objects.all().delete()
    
    print("[*] Creating Admin user...")
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@careersync.com',
        password='admin123',
        first_name='System',
        last_name='Admin'
    )
    
    print("[*] Creating Main User: Arka Karmoker...")
    arka_user = User.objects.create_user(
        username='arkakarmoker',
        email='karmokerarka@gmail.com',
        password='password123',
        first_name='Arka',
        last_name='Karmoker'
    )

    print("[*] Creating Categories...")
    cat_frontend = Category.objects.create(name='Frontend Development')
    cat_backend = Category.objects.create(name='Backend Development')
    cat_fullstack = Category.objects.create(name='Fullstack Engineering')
    cat_devops = Category.objects.create(name='DevOps & Cloud')
    cat_ai = Category.objects.create(name='AI & Data Engineering')
    cat_mobile = Category.objects.create(name='Mobile Development')

    now = timezone.now()

    # Detailed Job Descriptions
    jd_netflix = """Netflix is looking for a Senior Frontend Engineer to build high-performance user interfaces for our web platform serving over 200 million global members.
    
Key Responsibilities:
- Architect and develop scalable web applications using React, TypeScript, and modern state management.
- Optimize client-side render performance and core web vitals across devices.
- Collaborate with UI/UX designers and micro-frontend platform teams.

Requirements:
- 5+ years of experience with React, JavaScript (ES6+), HTML5, and Tailwind CSS.
- Proven track record of improving web performance and page load metrics.
- Experience with Next.js, GraphQL, and micro-frontend architectures."""

    jd_spotify = """Spotify is seeking a Backend Engineer (Python/Django) to design and scale APIs powering personalized audio recommendation engines.

Responsibilities:
- Build, deploy, and maintain RESTful and gRPC services using Python, Django, and FastAPI.
- Design database schemas and optimize query performance in PostgreSQL and Redis.
- Participate in architectural reviews and automated CI/CD deployment pipelines.

Requirements:
- 4+ years of professional backend experience with Python and Django.
- Experience handling high-concurrency workloads and caching strategies.
- Strong understanding of Docker, Kubernetes, and GCP."""

    jd_stripe = """Stripe is hiring a Staff Fullstack Engineer to drive core merchant onboarding and billing infrastructure.

Responsibilities:
- Build end-to-end features spanning React frontend interfaces and robust backend ledger APIs.
- Deliver bulletproof financial workflows with 99.999% uptime guarantees.
- Mentor junior engineers and collaborate directly with product owners.

Requirements:
- 6+ years of fullstack software engineering experience.
- Deep expertise in React, TypeScript, Python/Ruby, and relational databases.
- Passion for developer tooling, security, and developer experience."""

    jd_openai = """OpenAI is looking for an AI Application Engineer to build developer tools, SDK interfaces, and enterprise dashboard features for state-of-the-art LLMs.

Responsibilities:
- Implement prompt evaluation pipelines, streaming chat interfaces, and vector store integrations.
- Connect enterprise backend Python APIs with modern React single-page applications.

Requirements:
- Strong experience with Python (FastAPI/Django), PyTorch/LangChain, and React.
- Understanding of LLM architectures, embeddings, and vector databases (Pinecone/Chroma)."""

    jd_aws = """AWS is looking for a DevOps & Cloud Architect to lead cloud-native container deployments and infrastructure-as-code automation for enterprise migration teams.

Responsibilities:
- Write modular Infrastructure-as-Code using Terraform and CloudFormation.
- Configure multi-region Kubernetes (EKS) clusters and automated Github Actions / GitLab CI pipelines.

Requirements:
- Deep expertise in AWS ecosystem, Terraform, Kubernetes, Docker, and Linux administration."""

    jd_uber = """Uber is seeking a Mobile Software Engineer (React Native) to elevate the rider experience across mobile platforms.

Responsibilities:
- Build fluid, real-time tracking screens and payment checkout flows in React Native.
- Optimize mobile bundle size, memory usage, and native iOS/Android bridge performance."""

    jd_shopify = """Shopify is hiring a Fullstack Engineer to expand global merchant storefront customization tools.

Responsibilities:
- Maintain high-scale GraphQL endpoints and React storefront design engine components."""

    print("[*] Creating Rich Real-World Job Applications...")

    # 1. Netflix - Interview Status
    app1 = JobApplication.objects.create(
        user=arka_user,
        job_title='Senior Frontend Engineer',
        company_name='Netflix',
        job_description=jd_netflix,
        location='Remote',
        salary='$160,000 - $190,000',
        job_url='https://jobs.netflix.com/jobs/847291',
        application_date=(now - timedelta(days=12)).date(),
        status='Interview',
        category=cat_frontend,
        tags='React, TypeScript, Tailwind CSS, Next.js, Performance',
        notes='Referred by Sarah from LinkedIn. Passed initial technical phone screen with flying colors!'
    )

    # 2. Spotify - Screening Status
    app2 = JobApplication.objects.create(
        user=arka_user,
        job_title='Backend Engineer (Python / Django)',
        company_name='Spotify',
        job_description=jd_spotify,
        location='New York, NY (Hybrid)',
        salary='$150,000 + Equity',
        job_url='https://lifeatspotify.com/jobs/backend-engineer-python',
        application_date=(now - timedelta(days=6)).date(),
        status='Screening',
        category=cat_backend,
        tags='Python, Django, PostgreSQL, Redis, Docker',
        notes='Applied on the company portal. Recruiter reached out to schedule initial HR introductory call.'
    )

    # 3. Stripe - Selected / Offer Received
    app3 = JobApplication.objects.create(
        user=arka_user,
        job_title='Staff Fullstack Engineer',
        company_name='Stripe',
        job_description=jd_stripe,
        location='San Francisco, CA',
        salary='$210,000 + $40,000 Equity',
        job_url='https://stripe.com/jobs/listing/staff-fullstack-engineer',
        application_date=(now - timedelta(days=35)).date(),
        status='Selected',
        category=cat_fullstack,
        tags='Fullstack, React, Python, PostgreSQL, Payments',
        notes='OFFER RECEIVED! Base $210k + stock options. Currently reviewing contract terms.'
    )

    # 4. OpenAI - Interview Status
    app4 = JobApplication.objects.create(
        user=arka_user,
        job_title='AI Application Engineer',
        company_name='OpenAI',
        job_description=jd_openai,
        location='San Francisco, CA (Hybrid)',
        salary='$200,000 - $240,000',
        job_url='https://openai.com/careers/ai-app-engineer',
        application_date=(now - timedelta(days=18)).date(),
        status='Interview',
        category=cat_ai,
        tags='Python, LLM, OpenAI API, FastAPI, React',
        notes='Completed HR screen. Next round is live system design and LLM integration coding.'
    )

    # 5. AWS - Applied Status
    app5 = JobApplication.objects.create(
        user=arka_user,
        job_title='DevOps & Cloud Architect',
        company_name='Amazon Web Services',
        job_description=jd_aws,
        location='Seattle, WA (Remote)',
        salary='$175,000',
        job_url='https://amazon.jobs/en/jobs/294012',
        application_date=(now - timedelta(days=3)).date(),
        status='Applied',
        category=cat_devops,
        tags='AWS, Terraform, Kubernetes, Docker, CI/CD',
        notes='Submitted custom resume tailored for AWS Cloud Architect competencies.'
    )

    # 6. Uber - Applied Status
    app6 = JobApplication.objects.create(
        user=arka_user,
        job_title='Mobile Software Engineer (React Native)',
        company_name='Uber Technologies',
        job_description=jd_uber,
        location='Chicago, IL (Hybrid)',
        salary='$145,000',
        job_url='https://uber.com/careers/mobile-engineer',
        application_date=(now - timedelta(days=4)).date(),
        status='Applied',
        category=cat_mobile,
        tags='React Native, Mobile, Redux, iOS, Android',
        notes='Submitted application directly via LinkedIn easy apply.'
    )

    # 7. Shopify - Rejected Status
    app7 = JobApplication.objects.create(
        user=arka_user,
        job_title='Fullstack Engineer',
        company_name='Shopify',
        job_description=jd_shopify,
        location='Remote',
        salary='$140,000',
        job_url='https://shopify.com/careers/fullstack',
        application_date=(now - timedelta(days=25)).date(),
        status='Rejected',
        category=cat_fullstack,
        tags='GraphQL, React, Ruby, Fullstack',
        notes='Reached technical round. Rejected due to their preference for native Ruby expertise.'
    )

    # 8. Canonical (Ubuntu) - Wishlist Status
    app8 = JobApplication.objects.create(
        user=arka_user,
        job_title='Lead Django Software Engineer',
        company_name='Canonical (Ubuntu)',
        job_description='Looking for a lead Python/Django engineer to build open source management portals.',
        location='Remote',
        salary='$135,000',
        job_url='https://canonical.com/careers/django-lead',
        application_date=None,
        status='Wishlist',
        category=cat_backend,
        tags='Python, Django, Linux, OpenSource',
        notes='Great remote culture. Planning to update GitHub projects before applying.'
    )

    # 9. Vercel - Wishlist Status
    app9 = JobApplication.objects.create(
        user=arka_user,
        job_title='Senior React / Next.js Core Engineer',
        company_name='Vercel',
        job_description='Join the core team responsible for Next.js web ecosystem tools and server components.',
        location='Remote',
        salary='$170,000',
        job_url='https://vercel.com/careers/core-engineer',
        application_date=None,
        status='Wishlist',
        category=cat_frontend,
        tags='Next.js, React, Edge Computing, TypeScript',
        notes='Dream role! Need to prepare demo video of recent Next.js side project.'
    )

    print("[*] Creating Realistic Interviews...")

    # Interviews for Netflix (Interview Status)
    Interview.objects.create(
        application=app1,
        interview_date=now - timedelta(days=4),
        interview_type='HR Screening',
        meeting_link='https://zoom.us/j/9876543210',
        interview_notes='Discussed career trajectory, salary requirements ($160k-$190k), and notice period. Recruiter was very positive.'
    )

    Interview.objects.create(
        application=app1,
        interview_date=now + timedelta(days=2, hours=3),
        interview_type='Technical Round',
        meeting_link='https://meet.google.com/nfx-tech-interview',
        interview_notes='2-hour deep dive into React DOM reconciliation, custom hooks architecture, and micro-frontend state sync.'
    )

    # Interview for Spotify (Screening Status)
    Interview.objects.create(
        application=app2,
        interview_date=now + timedelta(days=4, hours=1),
        interview_type='HR Screening',
        meeting_link='https://spotify.zoom.us/j/4455667788',
        interview_notes='Initial chat with Spotify talent acquisition partner.'
    )

    # Interviews for Stripe (Selected / Offer Received)
    Interview.objects.create(
        application=app3,
        interview_date=now - timedelta(days=22),
        interview_type='HR Screening',
        meeting_link='https://stripe.zoom.us/j/111222333',
        interview_notes='Recruiter background call. Passed smoothly.'
    )

    Interview.objects.create(
        application=app3,
        interview_date=now - timedelta(days=14),
        interview_type='Technical Round',
        meeting_link='https://stripe.zoom.us/j/444555666',
        interview_notes='Live coding round building a multi-currency payment retry engine in Python.'
    )

    Interview.objects.create(
        application=app3,
        interview_date=now - timedelta(days=7),
        interview_type='Final Round',
        meeting_link='https://stripe.zoom.us/j/777888999',
        interview_notes='System design interview with VP of Engineering & Product Lead. Received official offer letter 3 days later!'
    )

    # Interviews for OpenAI (Interview Status)
    Interview.objects.create(
        application=app4,
        interview_date=now - timedelta(days=5),
        interview_type='HR Screening',
        meeting_link='https://openai.zoom.us/j/9988776655',
        interview_notes='Covered AI experience, familiarity with GPT models, and Python async backend patterns.'
    )

    Interview.objects.create(
        application=app4,
        interview_date=now + timedelta(days=5, hours=4),
        interview_type='Technical Round',
        meeting_link='https://openai.zoom.us/j/1122334455',
        interview_notes='Pair programming round on vector embeddings and high-throughput FastAPI streaming.'
    )

    print("[*] Creating Detailed AI Job Analyses...")

    # AI Analysis for Netflix
    JobAnalysis.objects.create(
        application=app1,
        job_summary='Senior Frontend role at Netflix building global UI web applications for 200M+ members with high performance requirements.',
        required_skills='React, TypeScript, HTML5, CSS3, Tailwind CSS, Next.js, Web Vitals, GraphQL',
        required_experience='5+ years of professional frontend software engineering experience',
        important_technologies='React, TypeScript, Next.js, Tailwind CSS, GraphQL, Jest/RTL',
        interview_preparation_suggestions='- Master Core Web Vitals (LCP, FID, CLS) and render cycle optimizations.\n- Brush up on React fiber architecture, memoization (useMemo/useCallback), and virtualized lists.\n- Prepare examples of micro-frontend architecture communication patterns.'
    )

    # AI Analysis for Spotify
    JobAnalysis.objects.create(
        application=app2,
        job_summary='Backend Python/Django engineering role focused on constructing APIs and audio recommendation infrastructure.',
        required_skills='Python, Django, FastAPI, PostgreSQL, Redis, gRPC, Docker, Kubernetes',
        required_experience='4+ years of backend development experience using Python & Django',
        important_technologies='Python 3.11, Django ORM, PostgreSQL, Redis, Docker, GCP',
        interview_preparation_suggestions='- Review Django ORM query optimization (select_related, prefetch_related, indexing).\n- Study Redis caching strategies (Cache-Aside, Write-Through, TTL expiration).\n- Prepare system design solutions for distributed audio streaming API queues.'
    )

    # AI Analysis for Stripe
    JobAnalysis.objects.create(
        application=app3,
        job_summary='Staff Fullstack role leading financial billing infrastructure, merchant onboarding, and ledger systems.',
        required_skills='Fullstack Development, React, TypeScript, Python/Ruby, PostgreSQL, REST APIs, System Design',
        required_experience='6+ years in fullstack engineering with focus on high availability',
        important_technologies='React, TypeScript, Python, PostgreSQL, Stripe API, Docker',
        interview_preparation_suggestions='- Focus heavily on database transaction isolation levels and idempotent API design.\n- Practice designing financial ledger systems with exact once semantics.\n- Demonstrate strong leadership, code review culture, and engineering mentorship.'
    )

    # AI Analysis for OpenAI
    JobAnalysis.objects.create(
        application=app4,
        job_summary='AI Application Engineer position developing developer SDKs, streaming chat interfaces, and enterprise tools for LLMs.',
        required_skills='Python, FastAPI, PyTorch, LangChain, OpenAI API, Vector DBs, React, TypeScript',
        required_experience='3+ years building fullstack Python applications with AI/LLM integrations',
        important_technologies='Python, FastAPI, OpenAI API, LangChain, Pinecone, React',
        interview_preparation_suggestions='- Study Server-Sent Events (SSE) and WebSockets for streaming token responses.\n- Understand RAG (Retrieval-Augmented Generation) pipeline design and vector similarity search.\n- Be ready to write efficient async Python code with asyncio and FastAPI.'
    )

    print("\n[+] Database seeding completed successfully!")
    print("==================================================")
    print(" CREDENTIALS CREATED:")
    print("==================================================")
    print("1. ADMIN ACCOUNT (Superuser):")
    print("   Username: admin")
    print("   Password: admin123")
    print("\n2. MAIN USER ACCOUNT:")
    print("   Name:     Arka Karmoker")
    print("   Username: arkakarmoker")
    print("   Email:    karmokerarka@gmail.com")
    print("   Password: password123")
    print("==================================================")

if __name__ == '__main__':
    seed()
