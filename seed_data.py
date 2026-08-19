import os
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from tracker.models import JobApplication, Interview, JobAnalysis, Category

def seed():
    print("[*] Clearing all existing database records for a fresh start...")
    JobAnalysis.objects.all().delete()
    Interview.objects.all().delete()
    JobApplication.objects.all().delete()
    Category.objects.all().delete()
    User.objects.all().delete()

    print("[*] Creating Admin superuser (admin / admin123)...")
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@careersync.com',
        password='admin123',
        first_name='System',
        last_name='Admin'
    )

    print("[*] Creating Main User: Arka Karmoker (arkakarmoker / password123)...")
    arka_user = User.objects.create_user(
        username='arkakarmoker',
        email='karmokerarka@gmail.com',
        password='password123',
        first_name='Arka',
        last_name='Karmoker'
    )

    print("[*] Creating Job Categories...")
    cat_frontend = Category.objects.create(name='Frontend Development')
    cat_backend = Category.objects.create(name='Backend Development')
    cat_fullstack = Category.objects.create(name='Fullstack Engineering')
    cat_devops = Category.objects.create(name='DevOps & Cloud Infrastructure')
    cat_ai = Category.objects.create(name='AI & Data Engineering')
    cat_mobile = Category.objects.create(name='Mobile App Development')
    cat_design = Category.objects.create(name='UI/UX & Product Design')
    cat_security = Category.objects.create(name='Cybersecurity & Infra')

    now = timezone.now()

    # Raw list of 32 detailed real-world job postings
    job_templates = [
        {
            'company': 'Netflix',
            'title': 'Senior Frontend Engineer',
            'category': cat_frontend,
            'location': 'Remote (US)',
            'salary': '$170,000 - $210,000',
            'url': 'https://jobs.netflix.com/jobs/sr-frontend-8472',
            'status': 'Interview',
            'days_ago': 14,
            'tags': 'React, TypeScript, Tailwind CSS, Next.js, Micro-frontends',
            'notes': 'Referred by Sarah from LinkedIn. Passed technical phone screen. 2nd round scheduled.',
            'desc': 'Netflix is looking for a Senior Frontend Engineer to build high-performance user interfaces for our web platform serving over 200M members worldwide. Key focus on Core Web Vitals, SSR, and micro-frontend architecture.'
        },
        {
            'company': 'Spotify',
            'title': 'Backend Engineer (Python / Django)',
            'category': cat_backend,
            'location': 'New York, NY (Hybrid)',
            'salary': '$155,000 + Equity',
            'url': 'https://lifeatspotify.com/jobs/backend-python-django',
            'status': 'Screening',
            'days_ago': 8,
            'tags': 'Python, Django, PostgreSQL, Redis, gRPC, Docker',
            'notes': 'Applied on portal. Recruiter reached out for initial screening call.',
            'desc': 'Spotify is seeking a Backend Engineer (Python/Django) to design and scale APIs powering personalized audio recommendation engines, streaming queues, and artist metrics.'
        },
        {
            'company': 'Stripe',
            'title': 'Staff Fullstack Engineer',
            'category': cat_fullstack,
            'location': 'San Francisco, CA',
            'salary': '$215,000 + $45,000 Equity',
            'url': 'https://stripe.com/jobs/listing/staff-fullstack',
            'status': 'Selected',
            'days_ago': 38,
            'tags': 'Fullstack, React, Python, PostgreSQL, Stripe API, Ledger',
            'notes': 'OFFER RECEIVED! Base $215k + equity. Negotiating start date.',
            'desc': 'Stripe is hiring a Staff Fullstack Engineer to lead merchant onboarding engines, international checkout workflows, and high-availability financial ledger services.'
        },
        {
            'company': 'OpenAI',
            'title': 'AI Application Engineer',
            'category': cat_ai,
            'location': 'San Francisco, CA (Hybrid)',
            'salary': '$210,000 - $250,000',
            'url': 'https://openai.com/careers/ai-app-engineer',
            'status': 'Interview',
            'days_ago': 20,
            'tags': 'Python, LLM, OpenAI API, LangChain, FastAPI, VectorDB',
            'notes': 'Completed HR screen. Next round is live system design and LLM integration coding.',
            'desc': 'Build developer tools, SDK interfaces, and enterprise dashboard features for state-of-the-art LLMs. Work directly with GPT models, embeddings, and vector databases.'
        },
        {
            'company': 'Amazon Web Services (AWS)',
            'title': 'DevOps & Cloud Architect',
            'category': cat_devops,
            'location': 'Seattle, WA (Remote)',
            'salary': '$180,000',
            'url': 'https://amazon.jobs/en/jobs/294012',
            'status': 'Applied',
            'days_ago': 4,
            'tags': 'AWS, Terraform, EKS, Kubernetes, Docker, CI/CD',
            'notes': 'Submitted custom resume tailored for AWS Cloud Architect competencies.',
            'desc': 'Lead cloud-native container deployments, multi-region Kubernetes (EKS) architectures, and Infrastructure-as-Code automation for enterprise migration teams.'
        },
        {
            'company': 'Uber Technologies',
            'title': 'Mobile Software Engineer (React Native)',
            'category': cat_mobile,
            'location': 'Chicago, IL (Hybrid)',
            'salary': '$148,000',
            'url': 'https://uber.com/careers/mobile-engineer-rn',
            'status': 'Applied',
            'days_ago': 5,
            'tags': 'React Native, Mobile, Redux, iOS, Android, WebSockets',
            'notes': 'Applied directly via LinkedIn easy apply.',
            'desc': 'Build fluid, real-time tracking screens and payment checkout flows in React Native. Optimize mobile bundle size, memory usage, and native bridges.'
        },
        {
            'company': 'Shopify',
            'title': 'Fullstack Developer',
            'category': cat_fullstack,
            'location': 'Remote (Canada / US)',
            'salary': '$140,000',
            'url': 'https://shopify.com/careers/fullstack-dev',
            'status': 'Rejected',
            'days_ago': 28,
            'tags': 'GraphQL, React, Ruby on Rails, Fullstack',
            'notes': 'Reached technical round. Rejected due to team preference for native Ruby background.',
            'desc': 'Expand global merchant storefront customization tools, custom liquid engine rendering, and high-scale GraphQL API endpoints.'
        },
        {
            'company': 'Canonical (Ubuntu)',
            'title': 'Lead Django Software Engineer',
            'category': cat_backend,
            'location': 'Remote',
            'salary': '$135,000',
            'url': 'https://canonical.com/careers/django-lead',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Python, Django, Linux, OpenSource, PostgreSQL',
            'notes': 'Great remote culture. Planning to update GitHub projects before applying.',
            'desc': 'Lead Python/Django engineer wanted to build open source infrastructure management portals and cloud distribution dashboards.'
        },
        {
            'company': 'Vercel',
            'title': 'Senior React / Next.js Core Engineer',
            'category': cat_frontend,
            'location': 'Remote',
            'salary': '$175,000',
            'url': 'https://vercel.com/careers/core-engineer',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Next.js, React, Server Components, TypeScript, V8',
            'notes': 'Dream role! Need to prepare demo video of recent Next.js side project.',
            'desc': 'Join the core team responsible for Next.js web ecosystem tools, React Server Components, compiler optimization, and edge network runtime engines.'
        },
        {
            'company': 'Google',
            'title': 'Software Infrastructure Engineer',
            'category': cat_backend,
            'location': 'Mountain View, CA',
            'salary': '$190,000 + Bonus',
            'url': 'https://careers.google.com/jobs/results/infra-eng',
            'status': 'Screening',
            'days_ago': 11,
            'tags': 'Go, C++, Distributed Systems, gRPC, Cloud Spanner',
            'notes': 'Recruiter reached out on LinkedIn. Recruiter screen call completed.',
            'desc': 'Design high-throughput distributed storage and RPC frameworks powering core Google Cloud internal services.'
        },
        {
            'company': 'Meta',
            'title': 'Senior Frontend Developer (React / GraphQL)',
            'category': cat_frontend,
            'location': 'Menlo Park, CA (Hybrid)',
            'salary': '$185,000 + RSU',
            'url': 'https://metacareers.com/jobs/sr-frontend-react',
            'status': 'Interview',
            'days_ago': 16,
            'tags': 'React, GraphQL, Relay, JavaScript, Performance',
            'notes': 'Coding interview scheduled for next Tuesday.',
            'desc': 'Architect interactive feeds and messaging web client components for Meta product ecosystem using Relay, GraphQL, and specialized React tooling.'
        },
        {
            'company': 'Microsoft',
            'title': 'Cloud Solutions Architect (Azure)',
            'category': cat_devops,
            'location': 'Redmond, WA',
            'salary': '$165,000',
            'url': 'https://careers.microsoft.com/jobs/azure-arch',
            'status': 'Applied',
            'days_ago': 7,
            'tags': 'Azure, Terraform, Enterprise, C#, Kubernetes',
            'notes': 'Applied via internal referral.',
            'desc': 'Help enterprise clients architect resilient hybrid-cloud architectures on Azure using containerized microservices and automated infrastructure deployment.'
        },
        {
            'company': 'Airbnb',
            'title': 'Lead Product Engineer',
            'category': cat_fullstack,
            'location': 'San Francisco, CA (Remote)',
            'salary': '$195,000',
            'url': 'https://careers.airbnb.com/positions/lead-product-eng',
            'status': 'Interview',
            'days_ago': 22,
            'tags': 'React, Java, Kotlin, Python, Design Systems',
            'notes': 'Pair programming interview went really well!',
            'desc': 'Build host management dashboards and guest booking checkout experiences with high visual polish, internationalization, and rapid feature iteration.'
        },
        {
            'company': 'GitHub',
            'title': 'Systems Engineer (Ruby / Go)',
            'category': cat_backend,
            'location': 'Remote',
            'salary': '$160,000',
            'url': 'https://github.com/about/careers/systems-eng',
            'status': 'Applied',
            'days_ago': 9,
            'tags': 'Go, Ruby, Git Internals, MySQL, Redis',
            'notes': 'Submitted resume highlighting git experience.',
            'desc': 'Maintain and scale backend repository storage clusters, git wire protocol handlers, and high-availability background job processors.'
        },
        {
            'company': 'Slack (Salesforce)',
            'title': 'Senior Backend Engineer (Realtime)',
            'category': cat_backend,
            'location': 'Denver, CO (Hybrid)',
            'salary': '$158,000',
            'url': 'https://slack.com/careers/backend-realtime',
            'status': 'Rejected',
            'days_ago': 42,
            'tags': 'Java, Hack/PHP, WebSockets, Redis, Kafka',
            'notes': 'Passed tech round, rejected after final architectural interview.',
            'desc': 'Build low-latency messaging servers handling millions of concurrent WebSocket connections and push notifications across enterprise workspaces.'
        },
        {
            'company': 'Figma',
            'title': 'Frontend Performance Engineer',
            'category': cat_frontend,
            'location': 'San Francisco, CA',
            'salary': '$180,000',
            'url': 'https://figma.com/careers/frontend-perf',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'WebAssembly, WebGL, Canvas API, TypeScript, React',
            'notes': 'Requires deep WebGL & C++ to Wasm compilation knowledge.',
            'desc': 'Optimize real-time multi-user canvas rendering, WebAssembly memory allocation, and vector graphic engines inside web browsers.'
        },
        {
            'company': 'Datadog',
            'title': 'Site Reliability Engineer (SRE)',
            'category': cat_devops,
            'location': 'New York, NY',
            'salary': '$168,000',
            'url': 'https://datadoghq.com/careers/sre',
            'status': 'Screening',
            'days_ago': 10,
            'tags': 'Python, Go, Kubernetes, Prometheus, Incident Response',
            'notes': 'Phone recruiter call completed. Technical assessment sent.',
            'desc': 'Ensure 99.99% reliability for telemetry data processing platforms collecting trillions of data points daily from cloud infrastructure.'
        },
        {
            'company': 'Snowflake',
            'title': 'Data Platform Engineer',
            'category': cat_ai,
            'location': 'San Mateo, CA',
            'salary': '$175,000',
            'url': 'https://snowflake.com/careers/data-platform-eng',
            'status': 'Applied',
            'days_ago': 12,
            'tags': 'Python, SQL, Spark, Data Pipelines, Cloud Storage',
            'notes': 'Applied directly on careers site.',
            'desc': 'Develop petabyte-scale data warehouse query optimizers and automated ETL streaming pipelines on cloud infrastructure.'
        },
        {
            'company': 'Discord',
            'title': 'Realtime Backend Engineer',
            'category': cat_backend,
            'location': 'Remote',
            'salary': '$165,000',
            'url': 'https://discord.com/careers/realtime-backend',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Elixir, Rust, WebSockets, Voice Engine, Redis',
            'notes': 'Awesome tech stack. Need to learn more Rust before applying.',
            'desc': 'Engineers building sub-millisecond voice, video, and text communication backend routing services for 150M+ active monthly users.'
        },
        {
            'company': 'Supabase',
            'title': 'Database Infrastructure Engineer',
            'category': cat_backend,
            'location': 'Remote',
            'salary': '$150,000',
            'url': 'https://supabase.com/careers/db-infra',
            'status': 'Applied',
            'days_ago': 3,
            'tags': 'PostgreSQL, Elixir, Go, Docker, Open Source',
            'notes': 'Applied via open source contribution link.',
            'desc': 'Build automated Postgres provisioning engines, real-time database listener plugins, and authentication middleware for open-source Firebase alternative.'
        },
        {
            'company': 'Anthropic',
            'title': 'AI Safety & Infrastructure Engineer',
            'category': cat_ai,
            'location': 'San Francisco, CA',
            'salary': '$220,000',
            'url': 'https://anthropic.com/careers/ai-infra',
            'status': 'Applied',
            'days_ago': 13,
            'tags': 'Python, PyTorch, Ray, GPU Clusters, Claude API',
            'notes': 'Submitted application with research portfolio.',
            'desc': 'Build large-scale GPU training cluster orchestration systems and evaluation environments for Claude AI models.'
        },
        {
            'company': 'Linear',
            'title': 'Frontend Engineer (React / TypeScript)',
            'category': cat_frontend,
            'location': 'Remote (Europe / US)',
            'salary': '$160,000',
            'url': 'https://linear.app/careers/frontend-engineer',
            'status': 'Interview',
            'days_ago': 19,
            'tags': 'React, TypeScript, GraphQL, Web Workers, IndexedDB',
            'notes': 'Completed take-home project! Review meeting scheduled.',
            'desc': 'Build lightning-fast, keyboard-first web interfaces with offline synchronization using IndexedDB and optimistic UI updates.'
        },
        {
            'company': 'Postman',
            'title': 'API Platform Engineer',
            'category': cat_backend,
            'location': 'Austin, TX (Hybrid)',
            'salary': '$142,000',
            'url': 'https://postman.com/careers/api-platform',
            'status': 'Applied',
            'days_ago': 15,
            'tags': 'Node.js, OpenAPI, Postman SDK, Microservices',
            'notes': 'Applied via company job portal.',
            'desc': 'Engineers constructing API testing automation tools, OpenAPI specification generators, and developer workspace synchronization services.'
        },
        {
            'company': 'Twilio',
            'title': 'Senior Telecom API Developer',
            'category': cat_backend,
            'location': 'Remote',
            'salary': '$152,000',
            'url': 'https://twilio.com/careers/telecom-api',
            'status': 'Rejected',
            'days_ago': 50,
            'tags': 'Java, Python, SIP, Telecom, REST APIs',
            'notes': 'Applied 2 months ago. Position filled internally.',
            'desc': 'Develop programmable voice, SMS, and SIP routing microservices delivering global communication connectivity.'
        },
        {
            'company': 'Atlassian',
            'title': 'Fullstack Engineer (Jira Core)',
            'category': cat_fullstack,
            'location': 'Remote (US)',
            'salary': '$150,000',
            'url': 'https://atlassian.com/careers/jira-fullstack',
            'status': 'Screening',
            'days_ago': 6,
            'tags': 'React, Java, Spring Boot, GraphQL, Microservices',
            'notes': 'HR recruiter call completed.',
            'desc': 'Build modern enterprise issue management boards and integration plugins serving millions of agile development teams.'
        },
        {
            'company': 'Databricks',
            'title': 'Distributed Systems Engineer',
            'category': cat_ai,
            'location': 'San Francisco, CA',
            'salary': '$195,000',
            'url': 'https://databricks.com/careers/dist-systems',
            'status': 'Applied',
            'days_ago': 11,
            'tags': 'Scala, Java, Apache Spark, Lakehouse, C++',
            'notes': 'Applied directly.',
            'desc': 'Design high-performance unified data analytics platform engines and distributed query processors for Lakehouse architectures.'
        },
        {
            'company': 'Cloudflare',
            'title': 'Edge Network Software Engineer',
            'category': cat_security,
            'location': 'Austin, TX',
            'salary': '$162,000',
            'url': 'https://cloudflare.com/careers/edge-eng',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Rust, Go, Cloudflare Workers, DNS, Security',
            'notes': 'Great company culture and edge technology.',
            'desc': 'Build DDoS protection, global DNS resolution, and Cloudflare Workers serverless edge execution platform components.'
        },
        {
            'company': 'HashiCorp',
            'title': 'Terraform Ecosystem Developer',
            'category': cat_devops,
            'location': 'Remote',
            'salary': '$155,000',
            'url': 'https://hashicorp.com/careers/terraform-dev',
            'status': 'Applied',
            'days_ago': 14,
            'tags': 'Go, Terraform, HCL, Cloud Providers, HCL2',
            'notes': 'Applied via custom referral link.',
            'desc': 'Develop official Terraform providers, core HCL language parser engines, and enterprise cloud infrastructure automation modules.'
        },
        {
            'company': 'Elastic',
            'title': 'Search Engine Backend Engineer',
            'category': cat_backend,
            'location': 'Remote',
            'salary': '$150,000',
            'url': 'https://elastic.co/careers/search-backend',
            'status': 'Applied',
            'days_ago': 17,
            'tags': 'Java, Lucene, Elasticsearch, Search, Distributed',
            'notes': 'Submitted application on elastic.co.',
            'desc': 'Engineers building distributed vector search indices, inverted term lists, and Lucene search engine core algorithms.'
        },
        {
            'company': 'Coinbase',
            'title': 'Blockchain & Web3 Backend Developer',
            'category': cat_backend,
            'location': 'Remote',
            'salary': '$175,000',
            'url': 'https://coinbase.com/careers/web3-dev',
            'status': 'Rejected',
            'days_ago': 60,
            'tags': 'Go, Ethereum, Solidity, Cryptography, REST',
            'notes': 'Position closed before interview process completed.',
            'desc': 'Develop secure crypto transaction indexers, smart contract verification tools, and high-frequency exchange order matching nodes.'
        },
        {
            'company': 'Docker',
            'title': 'Container Platform Developer',
            'category': cat_devops,
            'location': 'Remote',
            'salary': '$158,000',
            'url': 'https://docker.com/careers/container-dev',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Go, Docker Desktop, containerd, Linux Containers',
            'notes': 'Intrigued by recent Docker Desktop innovations.',
            'desc': 'Build container engine runtimes, buildkit image compilation engines, and developer desktop virtualization layers.'
        },
        {
            'company': 'JetBrains',
            'title': 'IDE Platform Developer',
            'category': cat_backend,
            'location': 'Remote (Europe / US)',
            'salary': '$145,000',
            'url': 'https://jetbrains.com/careers/ide-developer',
            'status': 'Applied',
            'days_ago': 8,
            'tags': 'Kotlin, Java, AST Parsers, IDE, Static Analysis',
            'notes': 'Applied with Kotlin project portfolio.',
            'desc': 'Engineers building static code analysis parsers, refactoring engines, and smart autocomplete features for PyCharm and IntelliJ IDEA.'
        }
    ]

    created_apps = []
    print("[*] Generating 32 detailed applications for Arka Karmoker...")
    for tmpl in job_templates:
        app_date = (now - timedelta(days=tmpl['days_ago'])).date() if tmpl['days_ago'] is not None else None
        app = JobApplication.objects.create(
            user=arka_user,
            job_title=tmpl['title'],
            company_name=tmpl['company'],
            job_description=tmpl['desc'],
            location=tmpl['location'],
            salary=tmpl['salary'],
            job_url=tmpl['url'],
            application_date=app_date,
            status=tmpl['status'],
            category=tmpl['category'],
            tags=tmpl['tags'],
            notes=tmpl['notes']
        )
        created_apps.append(app)

    print("[*] Creating 15+ Detailed Interview Schedule Records...")
    # Link interviews to various created applications
    app_dict = {a.company_name: a for a in created_apps}

    # Netflix Interviews
    if 'Netflix' in app_dict:
        Interview.objects.create(
            application=app_dict['Netflix'],
            interview_date=now - timedelta(days=5, hours=2),
            interview_type='HR Screening',
            meeting_link='https://zoom.us/j/9876543210',
            interview_notes='Discussed career trajectory, salary requirements ($170k-$210k), and remote preferences.'
        )
        Interview.objects.create(
            application=app_dict['Netflix'],
            interview_date=now + timedelta(days=2, hours=3),
            interview_type='Technical Round',
            meeting_link='https://meet.google.com/nfx-tech-interview',
            interview_notes='2-hour deep dive into React DOM reconciliation, custom hooks architecture, and micro-frontend state sync.'
        )

    # Spotify Interviews
    if 'Spotify' in app_dict:
        Interview.objects.create(
            application=app_dict['Spotify'],
            interview_date=now + timedelta(days=3, hours=1),
            interview_type='HR Screening',
            meeting_link='https://spotify.zoom.us/j/4455667788',
            interview_notes='Initial chat with Spotify talent acquisition partner.'
        )

    # Stripe Interviews (Selected)
    if 'Stripe' in app_dict:
        Interview.objects.create(
            application=app_dict['Stripe'],
            interview_date=now - timedelta(days=25),
            interview_type='HR Screening',
            meeting_link='https://stripe.zoom.us/j/111222333',
            interview_notes='Recruiter background call. Passed smoothly.'
        )
        Interview.objects.create(
            application=app_dict['Stripe'],
            interview_date=now - timedelta(days=16),
            interview_type='Technical Round',
            meeting_link='https://stripe.zoom.us/j/444555666',
            interview_notes='Live coding round building a multi-currency payment retry engine in Python.'
        )
        Interview.objects.create(
            application=app_dict['Stripe'],
            interview_date=now - timedelta(days=9),
            interview_type='Final Round',
            meeting_link='https://stripe.zoom.us/j/777888999',
            interview_notes='System design interview with VP of Engineering & Product Lead. Received official offer letter!'
        )

    # OpenAI Interviews
    if 'OpenAI' in app_dict:
        Interview.objects.create(
            application=app_dict['OpenAI'],
            interview_date=now - timedelta(days=4),
            interview_type='HR Screening',
            meeting_link='https://openai.zoom.us/j/9988776655',
            interview_notes='Covered AI experience, familiarity with GPT models, and Python async backend patterns.'
        )
        Interview.objects.create(
            application=app_dict['OpenAI'],
            interview_date=now + timedelta(days=5, hours=4),
            interview_type='Technical Round',
            meeting_link='https://openai.zoom.us/j/1122334455',
            interview_notes='Pair programming round on vector embeddings and high-throughput FastAPI streaming.'
        )

    # Google Interviews
    if 'Google' in app_dict:
        Interview.objects.create(
            application=app_dict['Google'],
            interview_date=now + timedelta(days=6, hours=2),
            interview_type='Technical Round',
            meeting_link='https://meet.google.com/goog-tech-screen',
            interview_notes='Data structures and algorithm coding challenge on trees and dynamic programming.'
        )

    # Meta Interviews
    if 'Meta' in app_dict:
        Interview.objects.create(
            application=app_dict['Meta'],
            interview_date=now + timedelta(days=1, hours=5),
            interview_type='Technical Round',
            meeting_link='https://bluejeans.com/meta-interview',
            interview_notes='React frontend UI architecture interview constructing a real-time feed rendering component.'
        )

    # Airbnb Interviews
    if 'Airbnb' in app_dict:
        Interview.objects.create(
            application=app_dict['Airbnb'],
            interview_date=now - timedelta(days=2),
            interview_type='Technical Round',
            meeting_link='https://airbnb.zoom.us/j/123987456',
            interview_notes='Constructed interactive search filter system in React.'
        )
        Interview.objects.create(
            application=app_dict['Airbnb'],
            interview_date=now + timedelta(days=7, hours=2),
            interview_type='Final Round',
            meeting_link='https://airbnb.zoom.us/j/987123654',
            interview_notes='Cross-functional behavioral interview with Engineering Director and Design Lead.'
        )

    # Linear Interviews
    if 'Linear' in app_dict:
        Interview.objects.create(
            application=app_dict['Linear'],
            interview_date=now + timedelta(days=4, hours=6),
            interview_type='Final Round',
            meeting_link='https://linear.app/meet/interview-arka',
            interview_notes='Reviewing take-home assignment implementation and Web Worker synchronization strategy.'
        )

    # Datadog Interviews
    if 'Datadog' in app_dict:
        Interview.objects.create(
            application=app_dict['Datadog'],
            interview_date=now + timedelta(days=8, hours=3),
            interview_type='HR Screening',
            meeting_link='https://datadog.zoom.us/j/5544332211',
            interview_notes='SRE team introductory chat.'
        )

    # Atlassian Interviews
    if 'Atlassian' in app_dict:
        Interview.objects.create(
            application=app_dict['Atlassian'],
            interview_date=now + timedelta(days=2, hours=1),
            interview_type='HR Screening',
            meeting_link='https://atlassian.zoom.us/j/6677889900',
            interview_notes='Recruiter background call.'
        )

    print("[*] Creating Detailed AI Job Analysis Records...")

    # AI Analysis for Netflix
    if 'Netflix' in app_dict:
        JobAnalysis.objects.create(
            application=app_dict['Netflix'],
            job_summary='Senior Frontend role at Netflix building global UI web applications for 200M+ members with high performance requirements.',
            required_skills='React, TypeScript, HTML5, CSS3, Tailwind CSS, Next.js, Web Vitals, GraphQL',
            required_experience='5+ years of professional frontend software engineering experience',
            important_technologies='React, TypeScript, Next.js, Tailwind CSS, GraphQL, Jest/RTL',
            interview_preparation_suggestions='- Master Core Web Vitals (LCP, FID, CLS) and render cycle optimizations.\n- Brush up on React fiber architecture, memoization (useMemo/useCallback), and virtualized lists.\n- Prepare examples of micro-frontend architecture communication patterns.'
        )

    # AI Analysis for Spotify
    if 'Spotify' in app_dict:
        JobAnalysis.objects.create(
            application=app_dict['Spotify'],
            job_summary='Backend Python/Django engineering role focused on constructing APIs and audio recommendation infrastructure.',
            required_skills='Python, Django, FastAPI, PostgreSQL, Redis, gRPC, Docker, Kubernetes',
            required_experience='4+ years of backend development experience using Python & Django',
            important_technologies='Python 3.11, Django ORM, PostgreSQL, Redis, Docker, GCP',
            interview_preparation_suggestions='- Review Django ORM query optimization (select_related, prefetch_related, indexing).\n- Study Redis caching strategies (Cache-Aside, Write-Through, TTL expiration).\n- Prepare system design solutions for distributed audio streaming API queues.'
        )

    # AI Analysis for Stripe
    if 'Stripe' in app_dict:
        JobAnalysis.objects.create(
            application=app_dict['Stripe'],
            job_summary='Staff Fullstack role leading financial billing infrastructure, merchant onboarding, and ledger systems.',
            required_skills='Fullstack Development, React, TypeScript, Python/Ruby, PostgreSQL, REST APIs, System Design',
            required_experience='6+ years in fullstack engineering with focus on high availability',
            important_technologies='React, TypeScript, Python, PostgreSQL, Stripe API, Docker',
            interview_preparation_suggestions='- Focus heavily on database transaction isolation levels and idempotent API design.\n- Practice designing financial ledger systems with exact once semantics.\n- Demonstrate strong leadership, code review culture, and engineering mentorship.'
        )

    # AI Analysis for OpenAI
    if 'OpenAI' in app_dict:
        JobAnalysis.objects.create(
            application=app_dict['OpenAI'],
            job_summary='AI Application Engineer position developing developer SDKs, streaming chat interfaces, and enterprise tools for LLMs.',
            required_skills='Python, FastAPI, PyTorch, LangChain, OpenAI API, Vector DBs, React, TypeScript',
            required_experience='3+ years building fullstack Python applications with AI/LLM integrations',
            important_technologies='Python, FastAPI, OpenAI API, LangChain, Pinecone, React',
            interview_preparation_suggestions='- Study Server-Sent Events (SSE) and WebSockets for streaming token responses.\n- Understand RAG (Retrieval-Augmented Generation) pipeline design and vector similarity search.\n- Be ready to write efficient async Python code with asyncio and FastAPI.'
        )

    # AI Analysis for Google
    if 'Google' in app_dict:
        JobAnalysis.objects.create(
            application=app_dict['Google'],
            job_summary='Software Infrastructure Engineer designing high-throughput distributed storage and RPC frameworks powering core Google Cloud services.',
            required_skills='Go, C++, Distributed Systems, gRPC, Cloud Spanner, Multithreading, Linux Internals',
            required_experience='4+ years of low-level systems programming or cloud infrastructure development',
            important_technologies='Go, C++, gRPC, Protobuf, Linux, Distributed Consensus (Raft/Paxos)',
            interview_preparation_suggestions='- Review distributed systems consensus protocols (Paxos, Raft).\n- Practice low-level memory management and concurrency primitives.\n- Prepare for heavy algorithmic graph traversal and dynamic programming questions.'
        )

    # AI Analysis for Meta
    if 'Meta' in app_dict:
        JobAnalysis.objects.create(
            application=app_dict['Meta'],
            job_summary='Senior Frontend role building interactive social feeds and messaging clients with Relay, GraphQL, and specialized React tooling.',
            required_skills='React, JavaScript (ESNext), GraphQL, Relay, Web Performance, UI Component Systems',
            required_experience='5+ years building large-scale single-page applications',
            important_technologies='React, Relay, GraphQL, JavaScript, Hack, Flow/TypeScript',
            interview_preparation_suggestions='- Master Relay client-side query caching and fragment colocation.\n- Practice building complex UI components live without third-party library helpers.\n- Review browser event loop and DOM rendering pipelines.'
        )

    # AI Analysis for Airbnb
    if 'Airbnb' in app_dict:
        JobAnalysis.objects.create(
            application=app_dict['Airbnb'],
            job_summary='Lead Product Engineer driving host dashboards, guest booking flows, internationalization, and visual UI polish.',
            required_skills='React, TypeScript, Java/Kotlin, Design Systems, REST/GraphQL APIs, Web i18n',
            required_experience='5+ years of fullstack product development experience',
            important_technologies='React, TypeScript, Kotlin, Java, GraphQL, Figma',
            interview_preparation_suggestions='- Focus on product sense, trade-offs between UX speed and backend complexity.\n- Practice end-to-end frontend system design for booking reservation engines.\n- Review state management for multi-step checkout funnels.'
        )

    # AI Analysis for Linear
    if 'Linear' in app_dict:
        JobAnalysis.objects.create(
            application=app_dict['Linear'],
            job_summary='Frontend Engineer building keyboard-first, ultra-fast issue tracking software with local-first IndexedDB sync.',
            required_skills='React, TypeScript, IndexedDB, Web Workers, Optimistic UI, GraphQL, WebSockets',
            required_experience='4+ years in high-performance frontend or desktop-web development',
            important_technologies='React, TypeScript, IndexedDB, Web Workers, Tailwind CSS',
            interview_preparation_suggestions='- Review local-first architecture patterns (CRDTs, optimistic state resolution).\n- Practice offloading compute-heavy tasks to Web Workers.\n- Study keyboard shortcut event dispatching and focus ring trap management.'
        )

    print("\n[+] Database seeding completed successfully!")
    print("==================================================")
    print(" CREDENTIALS CREATED:")
    print("==================================================")
    print("1. ADMIN ACCOUNT (Superuser):")
    print("   Username: admin")
    print("   Password: admin123")
    print("\n2. MAIN USER ACCOUNT (Arka Karmoker):")
    print("   Username: arkakarmoker")
    print("   Email:    karmokerarka@gmail.com")
    print("   Password: password123")
    print(f"\n   -> Total Applications Seeded: {JobApplication.objects.count()}")
    print(f"   -> Total Interviews Seeded:   {Interview.objects.count()}")
    print(f"   -> Total AI Analyses Seeded:  {JobAnalysis.objects.count()}")
    print(f"   -> Total Categories Seeded:   {Category.objects.count()}")
    print("==================================================")

if __name__ == '__main__':
    seed()
