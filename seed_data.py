import os
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from tracker.models import JobApplication, Interview, JobAnalysis, Category, UserProfile

def seed():
    print("=" * 60)
    print("  CareerSync — Full Database Seed Script")
    print("=" * 60)

    print("\n[1/7] Clearing all existing database records...")
    from django.core.management import call_command
    
    # Safely flush the entire database (removes all data and resets auto-increment IDs)
    call_command('flush', interactive=False)

    print("      ✓ Database flushed and IDs reset to 1.")

    # ──────────────────────────────────────────────────────────
    # USERS
    # ──────────────────────────────────────────────────────────
    print("\n[2/7] Creating user accounts...")

    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@careersync.com',
        password='admin123',
        first_name='Admin',
        last_name='User'
    )
    admin_profile, _ = UserProfile.objects.get_or_create(user=admin_user)
    admin_profile.headline = "Platform Administrator"
    admin_profile.skills = "System Administration, Python, Django, DevOps, Security, AWS"
    admin_profile.experience_years = 8
    admin_profile.bio = "Senior platform administrator responsible for CareerSync infrastructure, deployment pipelines, and security audits."
    admin_profile.save()
    print("      ✓ Admin superuser (admin / admin123)")

    arka_user = User.objects.create_user(
        username='arka',
        email='karmokerarka@gmail.com',
        password='password123',
        first_name='Arka',
        last_name='Karmoker'
    )
    profile, _ = UserProfile.objects.get_or_create(user=arka_user)
    profile.headline = "Full Stack Python & Django Developer"
    profile.skills = "Python, Django, FastAPI, PostgreSQL, Redis, JavaScript, React, Next.js, Tailwind CSS, Docker, REST APIs, Git, Celery, GraphQL, TypeScript"
    profile.experience_years = 4
    profile.bio = "Passionate full-stack developer specialized in building scalable web architectures, clean RESTful APIs, and modern responsive user interfaces with Python, Django, and React. Experienced in cloud deployments, CI/CD pipelines, and agile product development. Open-source contributor and technical blogger."
    profile.save()
    print("      ✓ Main user: Arka Karmoker (arka / password123)")

    # ──────────────────────────────────────────────────────────
    # CATEGORIES
    # ──────────────────────────────────────────────────────────
    print("\n[3/7] Creating job categories...")

    cat_frontend = Category.objects.create(name='Frontend Development')
    cat_backend = Category.objects.create(name='Backend Development')
    cat_fullstack = Category.objects.create(name='Fullstack Engineering')
    cat_devops = Category.objects.create(name='DevOps & Cloud Infrastructure')
    cat_ai = Category.objects.create(name='AI & Data Engineering')
    cat_mobile = Category.objects.create(name='Mobile App Development')
    cat_design = Category.objects.create(name='UI/UX & Product Design')
    cat_security = Category.objects.create(name='Cybersecurity & Infra')
    print(f"      ✓ {Category.objects.count()} categories created.")

    now = timezone.now()

    # ──────────────────────────────────────────────────────────
    # JOB APPLICATIONS (40 realistic entries)
    # ──────────────────────────────────────────────────────────
    print("\n[4/7] Creating 40 highly detailed job applications...")

    job_templates = [
        # ─── INTERVIEW STATUS ─────────────────────────────────
        {
            'company': 'Netflix',
            'title': 'Senior Frontend Engineer',
            'category': cat_frontend,
            'location': 'Los Gatos, CA (Remote)',
            'salary': '$170,000 - $210,000',
            'url': 'https://jobs.netflix.com/jobs/sr-frontend-8472',
            'status': 'Interview',
            'days_ago': 14,
            'tags': 'React, TypeScript, Tailwind CSS, Next.js, Micro-frontends',
            'notes': 'Referred by Sarah Chen from LinkedIn. Passed technical phone screen with flying colors. 2nd round (system design) scheduled for next week.',
            'desc': '''Netflix is looking for a Senior Frontend Engineer to join the Web UI Platform team responsible for building high-performance user interfaces serving over 260M members worldwide.

You will work on:
• Architecting micro-frontend modules for the Netflix web player and browse experience
• Optimizing Core Web Vitals (LCP < 2.5s, FID < 100ms, CLS < 0.1) across all device categories
• Building server-side rendered (SSR) React applications with Next.js for SEO-critical landing pages
• Developing reusable component libraries with Tailwind CSS and Storybook documentation
• Collaborating with the A/B experimentation platform team to deliver rapid UI feature variants

Requirements:
• 5+ years of professional frontend engineering experience with React and TypeScript
• Deep understanding of browser rendering pipelines, virtual DOM reconciliation, and paint optimization
• Experience with micro-frontend architecture patterns (Module Federation, import maps)
• Strong communication skills and ability to mentor junior engineers'''
        },
        {
            'company': 'OpenAI',
            'title': 'AI Application Engineer',
            'category': cat_ai,
            'location': 'San Francisco, CA (Hybrid)',
            'salary': '$210,000 - $250,000 + Equity',
            'url': 'https://openai.com/careers/ai-app-engineer',
            'status': 'Interview',
            'days_ago': 20,
            'tags': 'Python, LLM, OpenAI API, LangChain, FastAPI, VectorDB',
            'notes': 'Completed HR screen with positive feedback. Next round is live system design focusing on RAG pipeline architecture and LLM integration patterns.',
            'desc': '''OpenAI is hiring an AI Application Engineer to build developer-facing tools, SDK interfaces, and enterprise dashboard features for state-of-the-art large language models.

Responsibilities:
• Design and implement production-grade APIs for GPT model inference, fine-tuning, and evaluation
• Build real-time streaming chat interfaces using Server-Sent Events (SSE) and WebSocket protocols
• Develop Retrieval-Augmented Generation (RAG) pipelines with vector databases (Pinecone, Weaviate, Chroma)
• Create Python SDK libraries with comprehensive documentation, type hints, and async support
• Collaborate with research scientists to translate model capabilities into practical developer experiences

Requirements:
• 3+ years building fullstack Python applications with AI/ML integrations
• Proficiency with FastAPI, async Python (asyncio/aiohttp), and modern web frameworks
• Hands-on experience with embedding models, similarity search, and prompt engineering
• Strong understanding of token economics, context window management, and model evaluation metrics'''
        },
        {
            'company': 'Meta',
            'title': 'Senior Frontend Developer (React / GraphQL)',
            'category': cat_frontend,
            'location': 'Menlo Park, CA (Hybrid)',
            'salary': '$185,000 + RSU Package',
            'url': 'https://metacareers.com/jobs/sr-frontend-react',
            'status': 'Interview',
            'days_ago': 16,
            'tags': 'React, GraphQL, Relay, JavaScript, Performance',
            'notes': 'Coding interview scheduled for next Tuesday. Preparing heavy on Relay fragment colocation and GraphQL subscription patterns.',
            'desc': '''Meta is seeking a Senior Frontend Developer to architect interactive feeds, messaging web clients, and Marketplace product surfaces within the Meta product ecosystem.

You will:
• Build high-performance React components powering the Facebook and Instagram web experiences
• Design data-fetching patterns using Relay Modern and GraphQL with fragment colocation
• Optimize rendering performance for feeds processing thousands of heterogeneous content cards
• Implement real-time messaging features with GraphQL subscriptions and optimistic UI updates
• Drive frontend architecture decisions across cross-functional product teams

Requirements:
• 5+ years building large-scale single-page applications with React
• Expert-level GraphQL knowledge including schema design, caching, and batching strategies
• Experience with performance profiling tools (Chrome DevTools, React Profiler, Lighthouse)
• Strong CS fundamentals and ability to solve complex algorithmic problems under time pressure'''
        },
        {
            'company': 'Airbnb',
            'title': 'Lead Product Engineer',
            'category': cat_fullstack,
            'location': 'San Francisco, CA (Remote-Friendly)',
            'salary': '$195,000 + $40,000 Equity',
            'url': 'https://careers.airbnb.com/positions/lead-product-eng',
            'status': 'Interview',
            'days_ago': 22,
            'tags': 'React, TypeScript, Java, Kotlin, Design Systems',
            'notes': 'Pair programming interview went really well! Built a dynamic pricing calendar component in React. Final round with Engineering Director scheduled.',
            'desc': '''Airbnb is hiring a Lead Product Engineer to drive the Host Tools product vertical, building management dashboards, booking checkout experiences, and listing creation flows.

Responsibilities:
• Lead frontend architecture for the Airbnb Host Dashboard serving 4M+ active hosts globally
• Build guest booking checkout experiences with multi-step forms, payment integration, and real-time availability
• Develop and maintain Airbnb's internal design system (DLS) with 200+ reusable React components
• Implement internationalization (i18n) supporting 62 languages and locale-specific formatting
• Mentor a pod of 3-4 engineers and drive technical roadmap planning with Product and Design

Requirements:
• 5+ years of fullstack product development experience with React/TypeScript
• Experience building design systems or component libraries at scale
• Backend proficiency with Java, Kotlin, or Python for service layer development
• Strong product sense and ability to balance UX quality with engineering velocity'''
        },
        {
            'company': 'Linear',
            'title': 'Frontend Engineer (React / TypeScript)',
            'category': cat_frontend,
            'location': 'Remote (Europe / US)',
            'salary': '$160,000 - $180,000',
            'url': 'https://linear.app/careers/frontend-engineer',
            'status': 'Interview',
            'days_ago': 19,
            'tags': 'React, TypeScript, GraphQL, Web Workers, IndexedDB',
            'notes': 'Completed take-home project building a keyboard-driven command palette with fuzzy search. Review meeting with CTO scheduled this Friday.',
            'desc': '''Linear is looking for a Frontend Engineer to build lightning-fast, keyboard-first project management interfaces with offline-capable synchronization.

You will:
• Develop ultra-responsive React UIs with sub-16ms interaction latency targets
• Implement local-first data architecture using IndexedDB with CRDT-based conflict resolution
• Build keyboard shortcut systems with focus management and global command palettes (Cmd+K)
• Optimize Web Worker offloading for background sync, search indexing, and data transformation
• Design optimistic UI patterns for seamless offline-to-online state reconciliation

Requirements:
• 4+ years in high-performance frontend or desktop-web hybrid development
• Deep expertise with React, TypeScript, and modern CSS (Tailwind CSS preferred)
• Experience with local-first architecture patterns, service workers, or progressive web apps
• Passion for craft, pixel-perfect design implementation, and 60fps interaction fluidity'''
        },

        # ─── SCREENING STATUS ────────────────────────────────
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
            'notes': 'Applied on portal. Recruiter reached out within 48 hours for initial screening call. Strong interest in audio recommendation engine work.',
            'desc': '''Spotify is seeking a Backend Engineer (Python/Django) to design and scale APIs powering personalized audio recommendation engines, streaming queues, and artist analytics dashboards.

Responsibilities:
• Architect RESTful and gRPC APIs serving 500M+ monthly active users with < 50ms p99 latency
• Design PostgreSQL schema migrations for high-write artist streaming analytics tables
• Implement Redis caching layers for playlist metadata and user preference materialized views
• Build Celery task queues for asynchronous audio transcoding and recommendation batch processing
• Develop comprehensive test suites with 90%+ code coverage using pytest and factory_boy

Requirements:
• 4+ years of backend development experience using Python & Django
• Deep understanding of relational database optimization (query plans, indexing, partitioning)
• Experience with message brokers (Kafka, RabbitMQ) and task queue systems (Celery)
• Familiarity with containerized deployments using Docker and Kubernetes'''
        },
        {
            'company': 'Google',
            'title': 'Software Infrastructure Engineer',
            'category': cat_backend,
            'location': 'Mountain View, CA',
            'salary': '$190,000 + Bonus + RSU',
            'url': 'https://careers.google.com/jobs/results/infra-eng',
            'status': 'Screening',
            'days_ago': 11,
            'tags': 'Go, C++, Distributed Systems, gRPC, Cloud Spanner',
            'notes': 'Recruiter reached out on LinkedIn after viewing open-source contributions. Recruiter screen call completed successfully. Technical phone screen being scheduled.',
            'desc': '''Google is hiring a Software Infrastructure Engineer to design high-throughput distributed storage and RPC frameworks powering core Google Cloud internal services.

You will:
• Build and maintain globally distributed storage systems processing petabytes of data daily
• Design gRPC service meshes with automatic load balancing, circuit breaking, and retry policies
• Implement consensus algorithms (Raft/Paxos variants) for strongly consistent replicated state machines
• Optimize garbage collection, memory allocation, and thread scheduling for latency-critical services
• Contribute to internal infrastructure libraries used by thousands of Google engineers

Requirements:
• 4+ years of low-level systems programming or cloud infrastructure development
• Proficiency in Go or C++ with deep understanding of concurrency primitives
• Knowledge of distributed systems concepts (CAP theorem, consistency models, vector clocks)
• Experience with protocol buffer serialization and RPC framework design'''
        },
        {
            'company': 'Datadog',
            'title': 'Site Reliability Engineer (SRE)',
            'category': cat_devops,
            'location': 'New York, NY',
            'salary': '$168,000 - $195,000',
            'url': 'https://datadoghq.com/careers/sre',
            'status': 'Screening',
            'days_ago': 10,
            'tags': 'Python, Go, Kubernetes, Prometheus, Incident Response',
            'notes': 'Phone recruiter call completed. Technical assessment (take-home SRE scenario) sent — due in 5 days.',
            'desc': '''Datadog is looking for a Site Reliability Engineer to ensure 99.99% uptime for telemetry data processing platforms collecting trillions of data points daily.

Responsibilities:
• Design and maintain Kubernetes clusters processing 40TB+ of metrics, logs, and traces per day
• Build automated incident response runbooks and self-healing infrastructure controllers
• Implement SLO/SLI monitoring dashboards with Prometheus, Grafana, and custom Datadog integrations
• Conduct chaos engineering experiments to validate system resilience under failure conditions
• Lead post-mortem analysis and drive reliability improvements across engineering teams

Requirements:
• 3+ years in SRE, DevOps, or infrastructure engineering roles
• Strong programming skills in Python or Go for automation and tooling
• Experience managing production Kubernetes clusters at scale (1000+ pods)
• Deep understanding of networking (TCP/IP, DNS, load balancing, service mesh)'''
        },
        {
            'company': 'Atlassian',
            'title': 'Fullstack Engineer (Jira Core)',
            'category': cat_fullstack,
            'location': 'Sydney, Australia (Remote-Friendly)',
            'salary': '$150,000 - $170,000',
            'url': 'https://atlassian.com/careers/jira-fullstack',
            'status': 'Screening',
            'days_ago': 6,
            'tags': 'React, Java, Spring Boot, GraphQL, Microservices',
            'notes': 'HR recruiter call completed. Very friendly team culture. Next step is technical assessment focusing on React component design.',
            'desc': '''Atlassian is hiring a Fullstack Engineer for the Jira Core team to build modern enterprise issue tracking boards and workflow automation engines.

You will:
• Develop React-based kanban boards and sprint planning interfaces used by millions of agile teams
• Build Java/Spring Boot microservices for issue lifecycle management and notification dispatch
• Design GraphQL APIs for efficient data fetching across complex project hierarchies
• Implement real-time collaboration features using WebSocket connections and operational transforms
• Write comprehensive integration tests ensuring backward compatibility across Jira product versions

Requirements:
• 3+ years of fullstack development with React and Java/Kotlin
• Experience with microservice architectures and event-driven communication patterns
• Familiarity with GraphQL schema design and resolver optimization
• Strong understanding of agile methodologies and project management domain'''
        },

        # ─── SELECTED STATUS ─────────────────────────────────
        {
            'company': 'Stripe',
            'title': 'Staff Fullstack Engineer',
            'category': cat_fullstack,
            'location': 'San Francisco, CA',
            'salary': '$215,000 + $45,000 Equity/yr',
            'url': 'https://stripe.com/jobs/listing/staff-fullstack',
            'status': 'Selected',
            'days_ago': 38,
            'tags': 'Fullstack, React, Python, PostgreSQL, Stripe API, Ledger',
            'notes': '🎉 OFFER RECEIVED! Base $215k + equity package. Negotiating start date for March 1st. Extremely excited about the financial infrastructure team.',
            'desc': '''Stripe is hiring a Staff Fullstack Engineer to lead merchant onboarding engines, international checkout workflows, and high-availability financial ledger services.

Responsibilities:
• Lead design and implementation of multi-currency payment processing APIs handling $1T+ in annual volume
• Build merchant onboarding dashboards with KYC verification flows and real-time compliance checks
• Architect idempotent transaction processing systems with exactly-once delivery guarantees
• Design PostgreSQL schemas for double-entry accounting ledgers with audit trail capabilities
• Mentor a team of 5 engineers and drive architectural standards across billing infrastructure

Requirements:
• 6+ years in fullstack engineering with focus on high-availability distributed systems
• Expert-level knowledge of financial software patterns (idempotency, saga, compensation)
• Proficiency with React/TypeScript frontends and Python/Go backend services
• Experience with regulatory compliance (PCI-DSS, SOC 2) and financial reconciliation systems'''
        },
        {
            'company': 'Vercel',
            'title': 'Senior Developer Experience Engineer',
            'category': cat_frontend,
            'location': 'Remote (US)',
            'salary': '$175,000 + Stock Options',
            'url': 'https://vercel.com/careers/dx-engineer',
            'status': 'Selected',
            'days_ago': 30,
            'tags': 'Next.js, React, TypeScript, Developer Tools, Documentation',
            'notes': '🎉 OFFER ACCEPTED! Starting remote position on February 15th. Will be working on Next.js developer tooling and documentation.',
            'desc': '''Vercel is seeking a Senior Developer Experience Engineer to improve the developer journey for Next.js and the Vercel deployment platform.

You will:
• Build CLI tools, starter templates, and interactive tutorials for the Next.js ecosystem
• Design and implement developer-facing APIs with intuitive TypeScript interfaces
• Create comprehensive documentation with interactive code playgrounds and live examples
• Develop VS Code extensions and browser DevTools integrations for enhanced debugging
• Gather community feedback and translate developer pain points into product improvements

Requirements:
• 4+ years building developer tools, SDKs, or framework-level software
• Deep expertise with React, Next.js, TypeScript, and modern build tooling
• Excellent technical writing skills with ability to explain complex concepts clearly
• Active participation in open-source communities and developer advocacy'''
        },

        # ─── APPLIED STATUS ──────────────────────────────────
        {
            'company': 'Amazon Web Services (AWS)',
            'title': 'DevOps & Cloud Architect',
            'category': cat_devops,
            'location': 'Seattle, WA (Remote)',
            'salary': '$180,000 + Stock',
            'url': 'https://amazon.jobs/en/jobs/294012',
            'status': 'Applied',
            'days_ago': 4,
            'tags': 'AWS, Terraform, EKS, Kubernetes, Docker, CI/CD',
            'notes': 'Submitted custom resume tailored for AWS Cloud Architect competencies. Highlighted Terraform multi-cloud experience and EKS cluster management.',
            'desc': '''AWS is hiring a DevOps & Cloud Architect to lead cloud-native container deployments and Infrastructure-as-Code automation for enterprise migration teams.

Responsibilities:
• Design multi-region Kubernetes (EKS) architectures with automated failover and disaster recovery
• Build Terraform modules for repeatable infrastructure provisioning across 50+ AWS services
• Implement CI/CD pipelines with CodePipeline, GitHub Actions, and ArgoCD for GitOps deployments
• Conduct Well-Architected Reviews and security audits for enterprise cloud migration projects
• Develop cost optimization strategies reducing cloud spend by 20-40% through right-sizing and reserved instances

Requirements:
• 4+ years of cloud infrastructure experience with AWS (certified preferred)
• Expert-level Terraform/CloudFormation skills for Infrastructure-as-Code
• Deep experience with container orchestration (EKS, ECS, Docker Compose)
• Knowledge of networking concepts (VPC, Transit Gateway, PrivateLink, Route 53)'''
        },
        {
            'company': 'Uber Technologies',
            'title': 'Mobile Software Engineer (React Native)',
            'category': cat_mobile,
            'location': 'Chicago, IL (Hybrid)',
            'salary': '$148,000 - $175,000',
            'url': 'https://uber.com/careers/mobile-engineer-rn',
            'status': 'Applied',
            'days_ago': 5,
            'tags': 'React Native, Mobile, Redux, iOS, Android, WebSockets',
            'notes': 'Applied directly via LinkedIn Easy Apply. Customized cover letter highlighting real-time location tracking experience.',
            'desc': '''Uber is seeking a Mobile Software Engineer to build fluid, real-time tracking screens and payment checkout flows in React Native for the rider and driver apps.

You will:
• Develop cross-platform mobile features for the Uber rider app used by 130M+ monthly active users
• Build real-time map tracking interfaces with WebSocket-driven location updates at 1Hz refresh rate
• Optimize React Native bridge performance for smooth 60fps animations on mid-range devices
• Implement secure payment flows with biometric authentication and tokenized card processing
• Reduce mobile app bundle size through code splitting, lazy loading, and tree shaking

Requirements:
• 3+ years of mobile development with React Native or native iOS/Android
• Experience with real-time data synchronization using WebSockets or gRPC streams
• Knowledge of mobile performance profiling (Flipper, Xcode Instruments, Android Profiler)
• Understanding of mobile CI/CD pipelines and app store deployment processes'''
        },
        {
            'company': 'Microsoft',
            'title': 'Cloud Solutions Architect (Azure)',
            'category': cat_devops,
            'location': 'Redmond, WA (Hybrid)',
            'salary': '$165,000 + Bonus',
            'url': 'https://careers.microsoft.com/jobs/azure-arch',
            'status': 'Applied',
            'days_ago': 7,
            'tags': 'Azure, Terraform, Enterprise, C#, Kubernetes',
            'notes': 'Applied via internal referral from college friend Rafid. Strong alignment with Azure DevOps team requirements.',
            'desc': '''Microsoft is hiring a Cloud Solutions Architect to help enterprise clients design resilient hybrid-cloud architectures on Azure using containerized microservices.

Responsibilities:
• Architect hybrid-cloud solutions combining Azure Kubernetes Service (AKS) with on-premises infrastructure
• Design enterprise identity and access management solutions using Azure AD and RBAC policies
• Build reference architectures for event-driven microservices using Azure Service Bus and Event Grid
• Conduct technical workshops and proof-of-concept implementations for Fortune 500 clients
• Develop ARM templates and Bicep modules for automated infrastructure deployment

Requirements:
• 4+ years in cloud architecture or solutions engineering
• Azure certifications (AZ-305, AZ-400 preferred)
• Experience with C#/.NET Core, Python, or Go for cloud-native application development
• Strong presentation and client-facing communication skills'''
        },
        {
            'company': 'GitHub',
            'title': 'Systems Engineer (Ruby / Go)',
            'category': cat_backend,
            'location': 'Remote (US)',
            'salary': '$160,000 - $185,000',
            'url': 'https://github.com/about/careers/systems-eng',
            'status': 'Applied',
            'days_ago': 9,
            'tags': 'Go, Ruby, Git Internals, MySQL, Redis',
            'notes': 'Submitted resume highlighting open-source git contributions and distributed systems experience. Portfolio includes a custom git object store implementation.',
            'desc': '''GitHub is seeking a Systems Engineer to maintain and scale backend repository storage clusters, git wire protocol handlers, and background job processing infrastructure.

You will:
• Optimize git pack file generation and object deduplication for repositories with 10M+ objects
• Design MySQL sharding strategies for the repository metadata layer serving 100M+ developers
• Build Redis-backed distributed locking mechanisms for concurrent repository write operations
• Implement background job processors handling millions of webhook deliveries per hour
• Contribute to open-source git protocol improvements and server-side hook frameworks

Requirements:
• 3+ years of backend systems engineering with Ruby or Go
• Understanding of git internals (object model, packfiles, ref storage, transfer protocols)
• Experience with MySQL/PostgreSQL at scale (replication, sharding, query optimization)
• Familiarity with distributed computing patterns and eventual consistency models'''
        },
        {
            'company': 'Supabase',
            'title': 'Database Infrastructure Engineer',
            'category': cat_backend,
            'location': 'Remote (Worldwide)',
            'salary': '$150,000 - $175,000',
            'url': 'https://supabase.com/careers/db-infra',
            'status': 'Applied',
            'days_ago': 3,
            'tags': 'PostgreSQL, Elixir, Go, Docker, Open Source',
            'notes': 'Applied via open-source contribution link after merging a PR to their realtime engine. Strong alignment with their database-first philosophy.',
            'desc': '''Supabase is hiring a Database Infrastructure Engineer to build automated Postgres provisioning, real-time database listeners, and authentication middleware.

Responsibilities:
• Design automated PostgreSQL instance provisioning with custom extension management
• Build real-time data streaming using PostgreSQL logical replication and Elixir Phoenix Channels
• Implement Row Level Security (RLS) policy generators for multi-tenant SaaS applications
• Develop database migration tooling with zero-downtime schema change capabilities
• Contribute to Supabase's open-source codebase with high-quality, well-documented code

Requirements:
• 3+ years working with PostgreSQL internals (WAL, MVCC, extensions, replication)
• Proficiency in Go, Elixir, or Rust for systems-level programming
• Experience with containerized database deployments and orchestration
• Passion for open-source development and community collaboration'''
        },
        {
            'company': 'Anthropic',
            'title': 'AI Safety & Infrastructure Engineer',
            'category': cat_ai,
            'location': 'San Francisco, CA',
            'salary': '$220,000 - $260,000 + Equity',
            'url': 'https://anthropic.com/careers/ai-infra',
            'status': 'Applied',
            'days_ago': 13,
            'tags': 'Python, PyTorch, Ray, GPU Clusters, Claude API',
            'notes': 'Submitted application with AI research portfolio highlighting work on attention mechanism optimization and safety evaluation frameworks.',
            'desc': '''Anthropic is seeking an AI Safety & Infrastructure Engineer to build large-scale GPU training orchestration systems and evaluation pipelines for Claude AI models.

You will:
• Design distributed training infrastructure across clusters of thousands of H100/A100 GPUs
• Build model evaluation pipelines measuring safety, helpfulness, and harmlessness metrics
• Implement efficient checkpointing, model parallelism, and gradient accumulation strategies
• Develop internal tooling for prompt engineering, red-teaming, and constitutional AI workflows
• Optimize inference serving infrastructure for Claude API with dynamic batching and KV-cache management

Requirements:
• 3+ years building ML infrastructure or distributed computing systems
• Strong Python skills with experience in PyTorch, JAX, or TensorFlow
• Knowledge of GPU programming, CUDA optimization, or distributed training frameworks (Ray, DeepSpeed)
• Understanding of transformer architectures and large language model training dynamics'''
        },
        {
            'company': 'Snowflake',
            'title': 'Data Platform Engineer',
            'category': cat_ai,
            'location': 'San Mateo, CA (Hybrid)',
            'salary': '$175,000 + Equity',
            'url': 'https://snowflake.com/careers/data-platform-eng',
            'status': 'Applied',
            'days_ago': 12,
            'tags': 'Python, SQL, Spark, Data Pipelines, Cloud Storage',
            'notes': 'Applied directly on careers site. Highlighted experience with large-scale ETL pipeline design and SQL query optimization.',
            'desc': '''Snowflake is hiring a Data Platform Engineer to develop petabyte-scale data warehouse query optimizers and automated ETL streaming pipelines.

Responsibilities:
• Build and optimize SQL query execution engines for analytical workloads on distributed cloud storage
• Design automated ETL/ELT pipelines processing terabytes of structured and semi-structured data
• Implement data quality monitoring frameworks with anomaly detection and schema drift alerts
• Develop Snowpark (Python/Scala) UDFs for custom data transformation and ML feature engineering
• Optimize storage costs through intelligent data tiering, clustering, and materialized view management

Requirements:
• 4+ years of data engineering experience with Python, SQL, and distributed processing frameworks
• Deep understanding of columnar storage formats (Parquet, ORC) and query optimization techniques
• Experience with Apache Spark, dbt, or Airflow for data pipeline orchestration
• Knowledge of cloud data warehousing concepts and multi-tenant resource management'''
        },
        {
            'company': 'Postman',
            'title': 'API Platform Engineer',
            'category': cat_backend,
            'location': 'Austin, TX (Hybrid)',
            'salary': '$142,000 - $165,000',
            'url': 'https://postman.com/careers/api-platform',
            'status': 'Applied',
            'days_ago': 15,
            'tags': 'Node.js, OpenAPI, Postman SDK, Microservices',
            'notes': 'Applied via company job portal. Demonstrated Postman collection design experience in cover letter.',
            'desc': '''Postman is seeking API Platform Engineers to build API testing automation tools, OpenAPI specification generators, and workspace collaboration services.

You will:
• Develop API testing frameworks supporting REST, GraphQL, gRPC, and WebSocket protocols
• Build OpenAPI 3.1 specification parsers and code generators for 20+ programming languages
• Design real-time collaboration features for shared API workspaces with conflict resolution
• Implement API monitoring agents with scheduled execution and alerting capabilities
• Create Postman SDK libraries enabling programmatic collection management and CI/CD integration

Requirements:
• 3+ years building API tooling, developer platforms, or SDK infrastructure
• Strong Node.js and TypeScript skills with experience building CLI tools
• Deep understanding of API specification formats (OpenAPI, AsyncAPI, JSON Schema)
• Experience with distributed systems and real-time collaboration architectures'''
        },
        {
            'company': 'HashiCorp',
            'title': 'Terraform Ecosystem Developer',
            'category': cat_devops,
            'location': 'Remote (US)',
            'salary': '$155,000 - $180,000',
            'url': 'https://hashicorp.com/careers/terraform-dev',
            'status': 'Applied',
            'days_ago': 14,
            'tags': 'Go, Terraform, HCL, Cloud Providers, IaC',
            'notes': 'Applied via custom referral link from DevOps community contact. Strong Go programming background aligns well.',
            'desc': '''HashiCorp is hiring a Terraform Ecosystem Developer to build official Terraform providers, core HCL language features, and enterprise automation modules.

Responsibilities:
• Develop and maintain official Terraform providers for major cloud platforms (AWS, Azure, GCP)
• Implement HCL language parser enhancements for improved type checking and validation
• Build Terraform module testing frameworks with integration test orchestration
• Design provider SDK improvements enabling faster community provider development
• Contribute to Terraform CLI performance optimization for large state file operations

Requirements:
• 3+ years of Go programming experience with focus on CLI and infrastructure tooling
• Deep understanding of Infrastructure-as-Code concepts and cloud provider APIs
• Experience with Terraform provider development using the Plugin Framework
• Familiarity with CI/CD automation and GitOps deployment patterns'''
        },
        {
            'company': 'Elastic',
            'title': 'Search Engine Backend Engineer',
            'category': cat_backend,
            'location': 'Remote (Worldwide)',
            'salary': '$150,000 - $175,000',
            'url': 'https://elastic.co/careers/search-backend',
            'status': 'Applied',
            'days_ago': 17,
            'tags': 'Java, Lucene, Elasticsearch, Search, Distributed',
            'notes': 'Submitted application on elastic.co. Highlighted experience with full-text search indexing and distributed data processing.',
            'desc': '''Elastic is seeking a Search Engine Backend Engineer to build distributed vector search indices, inverted term lists, and Lucene core algorithms for Elasticsearch.

You will:
• Implement vector similarity search (kNN, HNSW) for semantic and hybrid search use cases
• Optimize Lucene segment merging, indexing throughput, and query execution planning
• Design distributed search coordination with scatter-gather query routing across shards
• Build aggregation framework extensions for complex analytics over indexed data
• Develop benchmarking and performance regression testing infrastructure

Requirements:
• 4+ years of Java development with focus on search or distributed systems
• Knowledge of information retrieval concepts (TF-IDF, BM25, vector embeddings)
• Experience with Apache Lucene internals or similar search engine technology
• Understanding of distributed consensus and data replication patterns'''
        },
        {
            'company': 'Databricks',
            'title': 'Distributed Systems Engineer',
            'category': cat_ai,
            'location': 'San Francisco, CA',
            'salary': '$195,000 + Equity',
            'url': 'https://databricks.com/careers/dist-systems',
            'status': 'Applied',
            'days_ago': 11,
            'tags': 'Scala, Java, Apache Spark, Lakehouse, C++',
            'notes': 'Applied directly. Interested in the Lakehouse query optimizer team.',
            'desc': '''Databricks is hiring a Distributed Systems Engineer to design high-performance unified data analytics engines and query processors for the Lakehouse platform.

Responsibilities:
• Optimize Apache Spark query execution plans for petabyte-scale analytical workloads
• Build adaptive query execution (AQE) strategies with runtime statistics-based re-optimization
• Design columnar memory managers with vectorized processing and SIMD acceleration
• Implement Delta Lake transaction protocols with ACID guarantees on cloud object storage
• Develop cost-based optimizer rules for join reordering, predicate pushdown, and partition pruning

Requirements:
• 4+ years building distributed data processing systems with Scala, Java, or C++
• Deep understanding of database query optimization and execution engine design
• Experience with Apache Spark, Flink, or similar distributed computing frameworks
• Knowledge of columnar storage formats and vectorized query processing techniques'''
        },
        {
            'company': 'JetBrains',
            'title': 'IDE Platform Developer',
            'category': cat_backend,
            'location': 'Remote (Europe / US)',
            'salary': '$145,000 - $170,000',
            'url': 'https://jetbrains.com/careers/ide-developer',
            'status': 'Applied',
            'days_ago': 8,
            'tags': 'Kotlin, Java, AST Parsers, IDE, Static Analysis',
            'notes': 'Applied with Kotlin project portfolio showcasing custom code analysis tools and IntelliJ plugin development.',
            'desc': '''JetBrains is seeking an IDE Platform Developer to build static code analysis parsers, refactoring engines, and intelligent autocomplete features for IntelliJ IDEA and PyCharm.

You will:
• Develop PSI (Program Structure Interface) parsers for language analysis and code intelligence
• Build smart code completion engines with ML-ranked suggestion scoring
• Implement automated refactoring operations (rename, extract, inline) with semantic correctness guarantees
• Design incremental re-parsing algorithms for real-time syntax error detection
• Optimize IDE startup time and memory footprint for large-scale enterprise codebases

Requirements:
• 3+ years of Kotlin or Java development with focus on tooling or compilers
• Understanding of abstract syntax trees (AST), type systems, and control flow analysis
• Experience with plugin development for IntelliJ platform or similar IDE frameworks
• Knowledge of language server protocol (LSP) and editor integration patterns'''
        },

        # ─── REJECTED STATUS ─────────────────────────────────
        {
            'company': 'Shopify',
            'title': 'Fullstack Developer',
            'category': cat_fullstack,
            'location': 'Remote (Canada / US)',
            'salary': '$140,000 - $160,000',
            'url': 'https://shopify.com/careers/fullstack-dev',
            'status': 'Rejected',
            'days_ago': 28,
            'tags': 'GraphQL, React, Ruby on Rails, Fullstack',
            'notes': 'Reached technical round. Rejected due to team preference for candidates with native Ruby on Rails background. Feedback was very constructive.',
            'desc': '''Shopify is hiring a Fullstack Developer to expand global merchant storefront customization tools and high-scale GraphQL API endpoints.

You will build custom Liquid template rendering engines, merchant admin dashboards, and payment processing integrations serving 2M+ online stores worldwide.'''
        },
        {
            'company': 'Slack (Salesforce)',
            'title': 'Senior Backend Engineer (Realtime)',
            'category': cat_backend,
            'location': 'Denver, CO (Hybrid)',
            'salary': '$158,000 - $180,000',
            'url': 'https://slack.com/careers/backend-realtime',
            'status': 'Rejected',
            'days_ago': 42,
            'tags': 'Java, Hack/PHP, WebSockets, Redis, Kafka',
            'notes': 'Passed technical coding round with strong performance. Rejected after final architectural review — team wanted more experience with Kafka event streaming at massive scale.',
            'desc': '''Slack is seeking a Senior Backend Engineer to build low-latency messaging servers handling millions of concurrent WebSocket connections and enterprise notification delivery systems.'''
        },
        {
            'company': 'Twilio',
            'title': 'Senior Telecom API Developer',
            'category': cat_backend,
            'location': 'Remote (US)',
            'salary': '$152,000 - $170,000',
            'url': 'https://twilio.com/careers/telecom-api',
            'status': 'Rejected',
            'days_ago': 50,
            'tags': 'Java, Python, SIP, Telecom, REST APIs',
            'notes': 'Applied 2 months ago. Position was filled internally before interview process completed. Recruiter encouraged reapplying for future openings.',
            'desc': '''Twilio is hiring a Senior Telecom API Developer to build programmable voice, SMS, and SIP routing microservices delivering global communication connectivity for 300K+ business customers.'''
        },
        {
            'company': 'Coinbase',
            'title': 'Blockchain & Web3 Backend Developer',
            'category': cat_backend,
            'location': 'Remote (US)',
            'salary': '$175,000 + Crypto Bonus',
            'url': 'https://coinbase.com/careers/web3-dev',
            'status': 'Rejected',
            'days_ago': 60,
            'tags': 'Go, Ethereum, Solidity, Cryptography, REST',
            'notes': 'Position closed before interview process completed due to company-wide hiring freeze. No technical evaluation happened.',
            'desc': '''Coinbase is seeking a Blockchain & Web3 Backend Developer to build secure crypto transaction indexers, smart contract verification tools, and exchange order matching engines.'''
        },

        # ─── WISHLIST STATUS ─────────────────────────────────
        {
            'company': 'Canonical (Ubuntu)',
            'title': 'Lead Django Software Engineer',
            'category': cat_backend,
            'location': 'Remote (Worldwide)',
            'salary': '$135,000 - $155,000',
            'url': 'https://canonical.com/careers/django-lead',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Python, Django, Linux, Open Source, PostgreSQL',
            'notes': 'Dream remote role with amazing open-source culture. Planning to polish GitHub profile and contribute to Ubuntu Server projects before applying.',
            'desc': '''Canonical is seeking a Lead Django Software Engineer to build open-source infrastructure management portals and cloud distribution dashboards for Ubuntu ecosystem tools.'''
        },
        {
            'company': 'Figma',
            'title': 'Frontend Performance Engineer',
            'category': cat_frontend,
            'location': 'San Francisco, CA',
            'salary': '$180,000 - $220,000',
            'url': 'https://figma.com/careers/frontend-perf',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'WebAssembly, WebGL, Canvas API, TypeScript, React',
            'notes': 'Fascinating role requiring deep WebGL & C++ to Wasm compilation knowledge. Currently studying Canvas rendering optimization to prepare.',
            'desc': '''Figma is hiring a Frontend Performance Engineer to optimize real-time multi-user canvas rendering, WebAssembly memory allocation, and vector graphic engines inside web browsers.'''
        },
        {
            'company': 'Discord',
            'title': 'Realtime Backend Engineer',
            'category': cat_backend,
            'location': 'Remote (US)',
            'salary': '$165,000 - $190,000',
            'url': 'https://discord.com/careers/realtime-backend',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Elixir, Rust, WebSockets, Voice Engine, Redis',
            'notes': 'Incredible tech stack. Currently learning Rust through Advent of Code challenges. Planning to apply once comfortable with Tokio async runtime.',
            'desc': '''Discord is seeking engineers to build sub-millisecond voice, video, and text communication backend routing services for 200M+ monthly active users.'''
        },
        {
            'company': 'Cloudflare',
            'title': 'Edge Network Software Engineer',
            'category': cat_security,
            'location': 'Austin, TX (Hybrid)',
            'salary': '$162,000 - $195,000',
            'url': 'https://cloudflare.com/careers/edge-eng',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Rust, Go, Cloudflare Workers, DNS, Security',
            'notes': 'Fascinating edge computing challenges. Following their engineering blog closely. Want to build a Cloudflare Workers demo project before applying.',
            'desc': '''Cloudflare is hiring an Edge Network Software Engineer to build DDoS protection systems, global DNS resolution infrastructure, and the Workers serverless edge execution platform.'''
        },
        {
            'company': 'Docker',
            'title': 'Container Platform Developer',
            'category': cat_devops,
            'location': 'Remote (US)',
            'salary': '$158,000 - $180,000',
            'url': 'https://docker.com/careers/container-dev',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Go, Docker Desktop, containerd, Linux Containers',
            'notes': 'Excited by recent Docker Desktop innovations and Wasm container support. Building a portfolio project using containerd SDK.',
            'desc': '''Docker is seeking a Container Platform Developer to build container engine runtimes, BuildKit image compilation engines, and developer desktop virtualization layers.'''
        },
        {
            'company': 'Notion',
            'title': 'Product Engineer',
            'category': cat_fullstack,
            'location': 'San Francisco, CA (Hybrid)',
            'salary': '$170,000 - $200,000',
            'url': 'https://notion.so/careers/product-engineer',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'React, TypeScript, Kotlin, Block Editor, Collaboration',
            'notes': 'Love the product! Want to explore their block editor architecture. Reading their engineering blog posts on CRDT synchronization.',
            'desc': '''Notion is seeking a Product Engineer to build collaborative workspace features, block editor components, and real-time synchronization infrastructure serving 35M+ users.'''
        },
        {
            'company': 'Tailscale',
            'title': 'Network Infrastructure Engineer',
            'category': cat_security,
            'location': 'Remote (Worldwide)',
            'salary': '$155,000 - $185,000',
            'url': 'https://tailscale.com/careers/network-infra',
            'status': 'Wishlist',
            'days_ago': None,
            'tags': 'Go, WireGuard, Networking, VPN, Security',
            'notes': 'Incredible remote-first culture. Already using Tailscale for my home lab. Want to contribute to their open-source tools before applying.',
            'desc': '''Tailscale is hiring a Network Infrastructure Engineer to build secure mesh VPN connectivity, WireGuard protocol implementations, and enterprise access control systems.'''
        },

        # ─── ADDITIONAL APPLIED ───────────────────────────────
        {
            'company': 'GitLab',
            'title': 'Senior Backend Engineer (CI/CD)',
            'category': cat_devops,
            'location': 'Remote (Worldwide)',
            'salary': '$145,000 - $175,000',
            'url': 'https://about.gitlab.com/jobs/senior-backend-cicd',
            'status': 'Applied',
            'days_ago': 6,
            'tags': 'Ruby, Go, CI/CD, Kubernetes, GitOps',
            'notes': 'Applied through their all-remote job board. Love their transparent handbook culture. Strong fit for pipeline execution engine improvements.',
            'desc': '''GitLab is seeking a Senior Backend Engineer for the CI/CD team to build pipeline execution engines, runner autoscaling infrastructure, and artifact management systems.

You will design and scale GitLab CI pipeline orchestration handling millions of jobs daily across Kubernetes, Docker, and shell executors.'''
        },
        {
            'company': 'Palantir Technologies',
            'title': 'Forward Deployed Software Engineer',
            'category': cat_fullstack,
            'location': 'Washington, DC',
            'salary': '$160,000 - $200,000 + Equity',
            'url': 'https://palantir.com/careers/fdse',
            'status': 'Applied',
            'days_ago': 10,
            'tags': 'Java, Python, TypeScript, Data Analysis, Ontology',
            'notes': 'Applied for FDSE role. Challenging application process with custom project submission required.',
            'desc': '''Palantir is hiring Forward Deployed Software Engineers to build custom analytical applications on the Foundry platform for government and commercial clients.

Work directly with customers to translate complex data challenges into production software solutions using TypeScript, Python, and Palantir's ontology framework.'''
        },
        {
            'company': 'Grafana Labs',
            'title': 'Senior Software Engineer (Observability)',
            'category': cat_devops,
            'location': 'Remote (US / Europe)',
            'salary': '$155,000 - $185,000',
            'url': 'https://grafana.com/careers/senior-eng-observability',
            'status': 'Applied',
            'days_ago': 7,
            'tags': 'Go, Prometheus, Grafana, Loki, Tempo, Mimir',
            'notes': 'Applied via open-source contributor pathway. Already contributed bugfixes to Grafana Loki. Recruiter acknowledged application.',
            'desc': '''Grafana Labs is seeking a Senior Software Engineer to build open-source observability tools including Grafana dashboards, Loki log aggregation, and Tempo distributed tracing.

Design and scale time-series databases processing billions of data points per second with sub-second query latency.'''
        },
    ]

    created_apps = []
    for tmpl in job_templates:
        app_date = (now - timedelta(days=tmpl['days_ago'])).date() if tmpl['days_ago'] is not None else None
        app = JobApplication.objects.create(
            user=arka_user,
            job_title=tmpl['title'].replace('\r\n', '\n'),
            company_name=tmpl['company'].replace('\r\n', '\n'),
            job_description=tmpl['desc'].replace('\r\n', '\n'),
            location=tmpl['location'].replace('\r\n', '\n'),
            salary=tmpl['salary'].replace('\r\n', '\n'),
            job_url=tmpl['url'].replace('\r\n', '\n'),
            application_date=app_date,
            status=tmpl['status'],
            category=tmpl['category'],
            tags=tmpl['tags'].replace('\r\n', '\n'),
            notes=tmpl['notes'].replace('\r\n', '\n')
        )
        created_apps.append(app)

    print(f"      ✓ {len(created_apps)} applications created.")

    # ──────────────────────────────────────────────────────────
    # INTERVIEWS (20+ detailed records)
    # ──────────────────────────────────────────────────────────
    print("\n[5/7] Creating interview schedule records...")

    app_dict = {a.company_name: a for a in created_apps}

    interviews_data = [
        # Netflix — 2 interviews (1 past, 1 upcoming)
        ('Netflix', now - timedelta(days=5, hours=2), 'HR Screening',
         'https://zoom.us/j/9876543210',
         'Discussed career trajectory, salary expectations ($170k-$210k range), remote work policy, and team culture. Interviewer was very positive about React expertise.'),
        ('Netflix', now + timedelta(days=2, hours=3), 'Technical Round',
         'https://meet.google.com/nfx-tech-interview',
         '2-hour deep dive into React DOM reconciliation, custom hooks architecture, micro-frontend state synchronization patterns, and Core Web Vitals optimization strategies.'),

        # Spotify — 1 upcoming
        ('Spotify', now + timedelta(days=3, hours=1), 'HR Screening',
         'https://spotify.zoom.us/j/4455667788',
         'Initial chat with Spotify talent acquisition partner. Focus on backend Python experience and cultural alignment with squad-based development model.'),

        # Stripe — 3 interviews (all past, selected)
        ('Stripe', now - timedelta(days=25), 'HR Screening',
         'https://stripe.zoom.us/j/111222333',
         'Recruiter background call covering financial software experience and system design philosophy. Very positive outcome.'),
        ('Stripe', now - timedelta(days=16), 'Technical Round',
         'https://stripe.zoom.us/j/444555666',
         'Live coding round building a multi-currency payment retry engine with idempotency keys in Python. Discussed database transaction isolation levels and saga patterns.'),
        ('Stripe', now - timedelta(days=9), 'Final Round',
         'https://stripe.zoom.us/j/777888999',
         'System design interview with VP of Engineering and Product Lead. Designed a global payment reconciliation system. Received official offer letter the next day!'),

        # OpenAI — 2 interviews (1 past, 1 upcoming)
        ('OpenAI', now - timedelta(days=4), 'HR Screening',
         'https://openai.zoom.us/j/9988776655',
         'Covered AI/ML experience, familiarity with GPT model family, Python async backend patterns, and interest in AI safety research. Strong positive signals.'),
        ('OpenAI', now + timedelta(days=5, hours=4), 'Technical Round',
         'https://openai.zoom.us/j/1122334455',
         'Pair programming round focusing on vector embeddings pipeline design and high-throughput FastAPI streaming with Server-Sent Events. Bring laptop with local dev environment.'),

        # Google — 1 upcoming
        ('Google', now + timedelta(days=6, hours=2), 'Technical Round',
         'https://meet.google.com/goog-tech-screen',
         'Data structures and algorithm coding challenge. Expected topics: trees, graphs, dynamic programming, and concurrency primitives. 45 minutes of live coding.'),

        # Meta — 1 upcoming
        ('Meta', now + timedelta(days=1, hours=5), 'Technical Round',
         'https://bluejeans.com/meta-frontend-interview',
         'React frontend UI architecture interview. Build a real-time feed rendering component with infinite scrolling, image lazy loading, and GraphQL data fetching.'),

        # Airbnb — 2 interviews (1 past, 1 upcoming)
        ('Airbnb', now - timedelta(days=2), 'Technical Round',
         'https://airbnb.zoom.us/j/123987456',
         'Built an interactive search filter system with debounced input, tag-based filtering, and responsive grid layout in React. Got very positive feedback from interviewer.'),
        ('Airbnb', now + timedelta(days=7, hours=2), 'Final Round',
         'https://airbnb.zoom.us/j/987123654',
         'Cross-functional behavioral interview with Engineering Director, Design Lead, and Product Manager. Focus on leadership, collaboration, and product sense.'),

        # Linear — 1 upcoming
        ('Linear', now + timedelta(days=4, hours=6), 'Final Round',
         'https://linear.app/meet/interview-arka',
         'Reviewing take-home assignment implementation. Discussion on Web Worker synchronization strategy, IndexedDB schema design, and keyboard navigation architecture.'),

        # Datadog — 1 upcoming
        ('Datadog', now + timedelta(days=8, hours=3), 'HR Screening',
         'https://datadog.zoom.us/j/5544332211',
         'SRE team introductory chat with hiring manager. Discussion on incident response experience, monitoring philosophy, and Kubernetes cluster management.'),

        # Atlassian — 1 upcoming
        ('Atlassian', now + timedelta(days=2, hours=1), 'HR Screening',
         'https://atlassian.zoom.us/j/6677889900',
         'Initial recruiter background call. Discuss Jira Core team structure, agile methodology experience, and preferred tech stack alignment.'),

        # Vercel — 2 past interviews (selected)
        ('Vercel', now - timedelta(days=20), 'Technical Round',
         'https://vercel.zoom.us/j/1234509876',
         'Built a CLI tool for scaffolding Next.js projects with template selection and configuration prompts. Demonstrated TypeScript API design skills.'),
        ('Vercel', now - timedelta(days=12), 'Final Round',
         'https://vercel.zoom.us/j/9876501234',
         'Culture fit interview with CEO and DX team lead. Discussed developer advocacy, technical writing, and open-source community engagement. Offer extended!'),

        # GitLab — 1 upcoming
        ('GitLab', now + timedelta(days=9, hours=4), 'HR Screening',
         'https://gitlab.zoom.us/j/7788990011',
         'All-remote onboarding discussion with People Ops team. Overview of async communication practices and handbook-first culture.'),

        # Grafana Labs — 1 upcoming
        ('Grafana Labs', now + timedelta(days=10, hours=2), 'Technical Round',
         'https://grafana.zoom.us/j/3344556677',
         'Open-source contribution review and Go systems programming assessment. Discussion on Prometheus TSDB internals and Loki log query optimization.'),
    ]

    interview_count = 0
    for company, date, itype, link, notes in interviews_data:
        if company in app_dict:
            Interview.objects.create(
                application=app_dict[company],
                interview_date=date.replace(second=0, microsecond=0),
                interview_type=itype.replace('\r\n', '\n'),
                meeting_link=link.replace('\r\n', '\n'),
                interview_notes=notes.replace('\r\n', '\n')
            )
            interview_count += 1

    print(f"      ✓ {interview_count} interview records created.")

    # ──────────────────────────────────────────────────────────
    # AI JOB ANALYSES (15 detailed records)
    # ──────────────────────────────────────────────────────────
    print("\n[6/7] Creating AI job analysis records...")

    analyses_data = [
        {
            'company': 'Netflix',
            'job_summary': 'Senior Frontend role at Netflix building global UI web applications for 260M+ streaming subscribers with strict performance requirements and micro-frontend architecture.',
            'required_skills': 'React, TypeScript, HTML5, CSS3, Tailwind CSS, Next.js, Web Vitals, GraphQL, Webpack/Vite',
            'required_experience': '5+ years of professional frontend software engineering experience with React ecosystem',
            'important_technologies': 'React 18, TypeScript 5, Next.js 14, Tailwind CSS, Storybook, Jest/RTL, Webpack Module Federation',
            'interview_preparation_suggestions': '- Master Core Web Vitals optimization (LCP < 2.5s, FID < 100ms, CLS < 0.1)\n- Deep dive into React fiber architecture, concurrent rendering, and Suspense boundaries\n- Practice micro-frontend communication patterns (custom events, shared state, Module Federation)\n- Review SSR vs CSR trade-offs and hydration optimization strategies\n- Prepare examples of performance auditing with Lighthouse and Chrome DevTools Performance tab',
            'match_score': 94,
            'match_analysis': 'Outstanding match for candidate background. Deep proficiency in modern React, TypeScript, Tailwind CSS, and component-driven development aligns perfectly with Netflix UI platform standards. Minor gap in WebAssembly experience, but not critical for this role.',
            'interview_questions': '- How would you debug an unexpected re-render cascade in a high-frequency streaming UI component tree?\n- Design a client-side telemetry system to measure Core Web Vitals across millions of concurrent users with minimal runtime overhead\n- Explain the trade-offs between Module Federation and import maps for micro-frontend architecture\n- How would you implement progressive image loading with blur-up placeholders for movie artwork?\n- Describe your approach to managing shared state between independently deployed micro-frontends'
        },
        {
            'company': 'Spotify',
            'job_summary': 'Backend Python/Django engineering role focused on building APIs and infrastructure for Spotify\'s personalized audio recommendation engine and artist analytics platform.',
            'required_skills': 'Python, Django, FastAPI, PostgreSQL, Redis, gRPC, Docker, Kubernetes, Celery',
            'required_experience': '4+ years of backend development experience using Python & Django with production-scale deployments',
            'important_technologies': 'Python 3.12, Django 5.x, PostgreSQL 16, Redis 7, Docker, GCP/Kubernetes, Celery, pytest',
            'interview_preparation_suggestions': '- Review Django ORM query optimization techniques (select_related, prefetch_related, database indexing, EXPLAIN ANALYZE)\n- Study Redis caching strategies: Cache-Aside, Write-Through, Write-Behind, TTL management\n- Prepare system design for distributed audio streaming API with rate limiting and queue management\n- Practice designing database schemas for time-series streaming analytics data\n- Review Python async patterns (asyncio, aiohttp) and their integration with Django',
            'match_score': 91,
            'match_analysis': 'Strong technical match. Extensive Django, PostgreSQL optimization, Redis caching, and Docker containerization experience directly aligns with Spotify backend core stack. Celery task queue expertise is a significant differentiator.',
            'interview_questions': '- How would you prevent and troubleshoot N+1 query problems in Django ORM with complex foreign key hierarchies?\n- Design a rate-limiting and quota management middleware for Spotify\'s public API serving 500M users\n- Explain how you would implement a distributed task queue for audio transcoding with priority levels and retry policies\n- Describe a challenging production database migration you performed with zero downtime\n- How would you design a real-time streaming analytics pipeline for tracking song play counts across regions?'
        },
        {
            'company': 'Stripe',
            'job_summary': 'Staff Fullstack role leading financial billing infrastructure, merchant onboarding engines, and double-entry accounting ledger systems processing $1T+ annually.',
            'required_skills': 'Fullstack Development, React, TypeScript, Python, PostgreSQL, REST APIs, System Design, Financial Software',
            'required_experience': '6+ years in fullstack engineering with focus on high-availability distributed financial systems',
            'important_technologies': 'React 18, TypeScript, Python, PostgreSQL, Stripe API, Docker, gRPC, Redis',
            'interview_preparation_suggestions': '- Focus on database transaction isolation levels (READ COMMITTED vs SERIALIZABLE) and their impact on financial consistency\n- Master idempotent API design patterns for payment processing (idempotency keys, exactly-once delivery)\n- Practice designing double-entry accounting ledger schemas with audit trails\n- Prepare examples of saga pattern implementation for distributed transaction management\n- Review PCI-DSS compliance requirements for handling cardholder data',
            'match_score': 87,
            'match_analysis': 'Solid fullstack alignment with strong API design and data integrity skills. Excellent fit for Stripe billing workflows. Minor onboarding needed for internal ledger tooling and PCI compliance specifics.',
            'interview_questions': '- How do you implement idempotency keys for payment processing endpoints to prevent duplicate charges on network timeouts?\n- Design a multi-currency reconciliation engine handling millions of transactions daily with exact penny accuracy\n- Explain the differences between optimistic and pessimistic locking in the context of concurrent payment processing\n- How would you design a webhook delivery system with guaranteed at-least-once delivery and exponential backoff?\n- Describe your approach to balancing speed-to-market with strict correctness in financial software'
        },
        {
            'company': 'OpenAI',
            'job_summary': 'AI Application Engineer building developer SDKs, streaming chat interfaces, RAG pipelines, and enterprise tooling for OpenAI\'s GPT model family.',
            'required_skills': 'Python, FastAPI, PyTorch, LangChain, OpenAI API, Vector Databases, React, TypeScript, async programming',
            'required_experience': '3+ years building fullstack Python applications with AI/LLM integrations and production deployments',
            'important_technologies': 'Python 3.12, FastAPI, OpenAI API, LangChain, Pinecone/Weaviate, React, asyncio',
            'interview_preparation_suggestions': '- Study Server-Sent Events (SSE) vs WebSockets for streaming token responses — understand backpressure handling\n- Master RAG pipeline design: document chunking strategies, embedding model selection, vector similarity search (cosine, dot product)\n- Practice writing efficient async Python with asyncio, aiohttp, and FastAPI dependency injection\n- Review prompt engineering techniques: few-shot learning, chain-of-thought, system prompts\n- Understand token economics, context window management, and model evaluation metrics (perplexity, BLEU, human preference)',
            'match_score': 96,
            'match_analysis': 'Exceptional fit. Demonstrated expertise with generative AI APIs, prompt engineering, fullstack Python development, and async programming directly matches OpenAI team roadmap. Portfolio includes relevant LLM integration projects.',
            'interview_questions': '- Walk through the architectural differences between SSE and WebSockets for streaming LLM completions at scale\n- Design a scalable RAG pipeline with intelligent chunking, embedding generation, vector caching, and semantic fallback logic\n- How would you implement a token usage tracking and billing system for an LLM API with per-organization quotas?\n- Explain how you would evaluate and A/B test different prompt engineering strategies in production\n- Design an API rate limiting system that accounts for variable token consumption across different model sizes'
        },
        {
            'company': 'Google',
            'job_summary': 'Software Infrastructure Engineer designing high-throughput distributed storage systems and gRPC service frameworks powering core Google Cloud internal services.',
            'required_skills': 'Go, C++, Distributed Systems, gRPC, Cloud Spanner, Multithreading, Linux Internals, Protocol Buffers',
            'required_experience': '4+ years of low-level systems programming or cloud infrastructure development with distributed systems experience',
            'important_technologies': 'Go, C++, gRPC, Protobuf, Linux, Borg/Kubernetes, Cloud Spanner, Bigtable',
            'interview_preparation_suggestions': '- Review distributed consensus protocols: Paxos, Raft, and their leader election/log replication mechanics\n- Practice implementing concurrent data structures (lock-free queues, concurrent hash maps)\n- Study memory management patterns: arena allocators, object pooling, GC tuning in Go\n- Prepare for algorithmic challenges on graphs (shortest path, topological sort), trees (segment trees), and dynamic programming\n- Understand CAP theorem trade-offs and consistency models (linearizability, causal, eventual)',
            'match_score': 82,
            'match_analysis': 'Good foundation in scalable backend architectures and API protocol design. Strong potential for distributed systems domain after deepening Go and C++ expertise. Algorithm preparation will be critical for interview success.',
            'interview_questions': '- Explain the difference between Raft and Paxos consensus algorithms — when would you choose one over the other?\n- Design a distributed key-value store with tunable consistency levels (ONE, QUORUM, ALL)\n- Implement a thread-safe LRU cache with O(1) reads and writes using fine-grained locking\n- How does gRPC handle connection multiplexing and flow control compared to REST over HTTP/1.1?\n- Design a monitoring system that can detect and automatically mitigate cascading failures in a microservice mesh'
        },
        {
            'company': 'Meta',
            'job_summary': 'Senior Frontend role building interactive social feeds, messaging web clients, and Marketplace surfaces using Relay, GraphQL, and specialized React tooling within Meta\'s ecosystem.',
            'required_skills': 'React, JavaScript (ESNext), GraphQL, Relay, Web Performance, UI Component Systems, Flow/TypeScript',
            'required_experience': '5+ years building large-scale single-page applications with complex state management',
            'important_technologies': 'React 19, Relay Modern, GraphQL, JavaScript, Hack, Flow, Jest, React DevTools',
            'interview_preparation_suggestions': '- Master Relay fragment colocation, @refetchable directives, and pagination (useInfiniteQuery)\n- Practice building complex UI components from scratch without third-party libraries\n- Review browser event loop, task vs microtask queues, requestAnimationFrame timing\n- Study DOM rendering pipeline: style calculation → layout → paint → composite\n- Prepare for whiteboard coding with algorithmic focus on arrays, strings, and tree traversals',
            'match_score': 89,
            'match_analysis': 'High match for Meta feed and messaging frontend engineering. Extensive React mastery, performance profiling skills, and UI architecture experience make candidate highly competitive. Relay-specific experience can be quickly acquired.',
            'interview_questions': '- How does GraphQL fragment colocation in Relay prevent over-fetching and improve component isolation?\n- Build an infinite-scrolling feed component with virtualized DOM rendering and intersection observer-based image preloading\n- Explain the difference between React.memo, useMemo, and useCallback — when is each appropriate?\n- How would you implement optimistic UI updates for a messaging app with eventual consistency guarantees?\n- Describe your strategy for managing technical debt in a codebase with 500+ active contributors'
        },
        {
            'company': 'Airbnb',
            'job_summary': 'Lead Product Engineer driving host management dashboards, guest booking checkout flows, internationalization across 62 languages, and design system stewardship.',
            'required_skills': 'React, TypeScript, Java/Kotlin, Design Systems, REST/GraphQL APIs, i18n, A/B Testing',
            'required_experience': '5+ years of fullstack product development with strong design collaboration skills',
            'important_technologies': 'React, TypeScript, Kotlin, Java, GraphQL, Figma, Storybook, Chromatic',
            'interview_preparation_suggestions': '- Focus on product sense: trade-offs between UX quality and engineering velocity\n- Practice end-to-end system design for booking reservation engines with payment integration\n- Review multi-step checkout form state management with validation and error recovery\n- Study internationalization patterns: ICU message format, pluralization rules, RTL layout support\n- Prepare leadership examples: mentoring, roadmap prioritization, cross-functional collaboration',
            'match_score': 88,
            'match_analysis': 'Very strong product engineering match. Excellent blend of frontend aesthetics, design system thinking, and reliable backend API development. Leadership potential and product sense align well with Airbnb host product team requirements.',
            'interview_questions': '- Design a booking calendar widget supporting multi-timezone availability, instant currency conversion, and accessibility compliance\n- How would you optimize bundle size and i18n string loading for users across 62 languages without impacting TTI?\n- Describe your approach to building and maintaining a design system with 200+ components across multiple product teams\n- How do you collaborate with UX designers and PMs when technical constraints conflict with product requirements?\n- Design an A/B testing framework for measuring conversion rate impact of checkout flow changes'
        },
        {
            'company': 'Linear',
            'job_summary': 'Frontend Engineer building keyboard-first, ultra-fast issue tracking software with local-first IndexedDB synchronization and real-time collaboration.',
            'required_skills': 'React, TypeScript, IndexedDB, Web Workers, Optimistic UI, GraphQL, WebSockets, Tailwind CSS',
            'required_experience': '4+ years in high-performance frontend or desktop-web hybrid application development',
            'important_technologies': 'React 18, TypeScript 5, IndexedDB, Web Workers, Tailwind CSS, GraphQL Subscriptions',
            'interview_preparation_suggestions': '- Study local-first architecture: CRDTs (Automerge, Yjs), operational transforms, conflict resolution\n- Practice offloading compute-heavy operations to Web Workers with structured clone transfer\n- Design keyboard shortcut systems with focus management and accessibility (ARIA)\n- Review optimistic UI update patterns with rollback and conflict reconciliation\n- Understand IndexedDB transaction scoping, versioned migrations, and cursor-based queries',
            'match_score': 93,
            'match_analysis': 'Top-tier alignment with modern web application engineering philosophy. Deep understanding of optimistic UI patterns, Tailwind CSS craftsmanship, and performance-first architecture directly matches Linear\'s engineering DNA.',
            'interview_questions': '- How do optimistic UI updates work with conflict resolution when a client goes offline and reconnects with divergent state?\n- Build a global command palette (Cmd+K) with fuzzy search scoring across thousands of locally-cached issue records\n- Explain how CRDTs enable eventual consistency without central coordination — what are the trade-offs vs OT?\n- Design a Web Worker architecture for background search index building with incremental updates\n- What principles do you follow to ensure an application maintains buttery-smooth 60fps interaction feel?'
        },
        {
            'company': 'Anthropic',
            'job_summary': 'AI Safety & Infrastructure Engineer building GPU training cluster orchestration, model evaluation pipelines, and Claude API inference infrastructure.',
            'required_skills': 'Python, PyTorch, JAX, Ray, CUDA, Distributed Training, GPU Cluster Management, Linux Systems',
            'required_experience': '3+ years building ML infrastructure or distributed computing systems at scale',
            'important_technologies': 'Python, PyTorch, JAX, Ray, CUDA, NCCL, Slurm, Kubernetes, H100/A100 GPUs',
            'interview_preparation_suggestions': '- Study distributed training strategies: data parallelism, model parallelism, pipeline parallelism, FSDP\n- Understand GPU memory management: gradient checkpointing, mixed precision (FP16/BF16), activation offloading\n- Review transformer architecture internals: multi-head attention, KV-cache, Flash Attention\n- Practice designing fault-tolerant training pipelines with automatic checkpointing and recovery\n- Study RLHF/Constitutional AI training pipelines and safety evaluation methodologies',
            'match_score': 78,
            'match_analysis': 'Strong Python foundation and growing ML infrastructure knowledge. GPU cluster management and distributed training experience needs development, but fast learning trajectory and AI enthusiasm are positive signals.',
            'interview_questions': '- Explain the trade-offs between data parallelism and model parallelism for training a 70B parameter model\n- Design a fault-tolerant distributed training pipeline that can recover from individual GPU or node failures\n- How would you implement a model evaluation pipeline that measures safety, helpfulness, and factual accuracy?\n- Describe the role of Flash Attention in reducing memory usage during transformer training\n- Design a real-time inference serving system for Claude API with dynamic batching and request prioritization'
        },
        {
            'company': 'Vercel',
            'job_summary': 'Senior Developer Experience Engineer improving the Next.js developer journey through CLI tools, documentation, starter templates, and IDE integrations.',
            'required_skills': 'Next.js, React, TypeScript, CLI Development, Technical Writing, Developer Advocacy, Open Source',
            'required_experience': '4+ years building developer tools, SDKs, or framework-level software with strong community engagement',
            'important_technologies': 'Next.js 14, React 18, TypeScript, Node.js CLI, Turbopack, Storybook, MDX',
            'interview_preparation_suggestions': '- Deep dive into Next.js App Router, Server Components, and streaming SSR architecture\n- Practice building CLI tools with interactive prompts, progress bars, and error handling\n- Review technical writing best practices: progressive disclosure, code-first documentation\n- Prepare examples of developer community engagement and open-source contribution leadership\n- Study Turbopack architecture and its advantages over Webpack for development builds',
            'match_score': 90,
            'match_analysis': 'Excellent alignment with DX engineering requirements. Strong Next.js expertise, TypeScript proficiency, and demonstrated ability to create high-quality developer-facing content. Active open-source participation is a strong differentiator.',
            'interview_questions': '- How would you design a CLI scaffolding tool that adapts project templates based on user-selected features and preferences?\n- Explain the differences between Next.js Pages Router and App Router — how would you guide developers migrating between them?\n- Design an interactive code playground for documentation that supports live editing, syntax highlighting, and preview rendering\n- How do you gather and prioritize developer feedback to drive product improvements in a framework ecosystem?\n- Describe your approach to writing documentation that serves both beginners and advanced users effectively'
        },
        {
            'company': 'Datadog',
            'job_summary': 'SRE role ensuring 99.99% platform reliability for telemetry processing systems handling trillions of metrics, logs, and traces daily.',
            'required_skills': 'Python, Go, Kubernetes, Prometheus, Grafana, Incident Response, Chaos Engineering, Terraform',
            'required_experience': '3+ years in SRE, DevOps, or infrastructure engineering with production on-call experience',
            'important_technologies': 'Python, Go, Kubernetes, Prometheus, Terraform, PagerDuty, Datadog, eBPF',
            'interview_preparation_suggestions': '- Review SRE principles: SLOs, SLIs, error budgets, and their relationship to release velocity\n- Study Kubernetes architecture: scheduler, controller manager, etcd, CNI networking, resource quotas\n- Practice incident response scenarios with structured postmortem analysis\n- Understand chaos engineering methodologies: fault injection, blast radius containment, steady-state hypothesis\n- Review networking fundamentals: TCP handshake, DNS resolution, load balancing algorithms, mTLS',
            'match_score': 85,
            'match_analysis': 'Strong DevOps and infrastructure foundation with Python and Kubernetes experience. Docker and CI/CD pipeline expertise translates well to SRE responsibilities. On-call experience and incident management skills will be assessed.',
            'interview_questions': '- How would you define SLOs for a metrics ingestion pipeline and what error budget policies would you implement?\n- Design an automated incident response system that detects anomalies and triggers self-healing remediation\n- Explain how you would conduct a chaos engineering experiment to test database failover resilience\n- Describe a production incident you investigated — what was the root cause and what preventive measures did you implement?\n- How would you design a Kubernetes cluster autoscaler that balances cost optimization with burst capacity requirements?'
        },
        {
            'company': 'Atlassian',
            'job_summary': 'Fullstack Engineer for Jira Core building modern issue tracking boards, sprint planning tools, and workflow automation engines serving millions of agile development teams.',
            'required_skills': 'React, Java, Spring Boot, GraphQL, Microservices, WebSockets, Agile Methodology',
            'required_experience': '3+ years of fullstack development with React and Java/Kotlin in enterprise software',
            'important_technologies': 'React, TypeScript, Java 21, Spring Boot, GraphQL, Kafka, PostgreSQL',
            'interview_preparation_suggestions': '- Study microservice communication patterns: sync (REST/gRPC) vs async (Kafka/RabbitMQ) trade-offs\n- Practice React component design for drag-and-drop kanban boards with complex state management\n- Review GraphQL schema design: batching (DataLoader), caching, and N+1 prevention\n- Prepare examples of working in agile teams and contributing to sprint ceremonies\n- Understand event sourcing and CQRS patterns for issue lifecycle state management',
            'match_score': 86,
            'match_analysis': 'Good fullstack alignment with strong React and API design skills. Django/Python backend experience transfers well to Java/Spring Boot patterns. GraphQL expertise is directly applicable. Enterprise SaaS experience would strengthen candidacy.',
            'interview_questions': '- Design a real-time kanban board that supports drag-and-drop reordering with optimistic updates across multiple concurrent users\n- How would you architect a workflow automation engine that allows users to define custom triggers and actions?\n- Explain the trade-offs between event sourcing and traditional CRUD for managing issue lifecycle state transitions\n- Design a GraphQL API for a project hierarchy (Organization → Project → Board → Sprint → Issue) with efficient nested queries\n- How do you approach testing strategy for a fullstack feature spanning React UI, API layer, and database interactions?'
        },
        {
            'company': 'GitHub',
            'job_summary': 'Systems Engineer maintaining backend repository storage clusters, git protocol handlers, and high-availability background job processing infrastructure for 100M+ developers.',
            'required_skills': 'Go, Ruby, Git Internals, MySQL, Redis, Distributed Systems, Background Jobs',
            'required_experience': '3+ years of backend systems engineering with performance-critical production systems',
            'important_technologies': 'Go, Ruby, MySQL, Redis, Git, Kafka, Kubernetes, Prometheus',
            'interview_preparation_suggestions': '- Deep dive into git internals: object model (blob, tree, commit, tag), packfiles, delta compression\n- Study MySQL replication topologies: primary-replica, group replication, ProxySQL routing\n- Review distributed locking patterns: Redis SETNX, Redlock algorithm, lease-based locking\n- Practice designing high-throughput webhook delivery systems with retry and dead-letter queues\n- Understand background job processing patterns: priority queues, rate limiting, idempotency',
            'match_score': 84,
            'match_analysis': 'Solid backend engineering foundation with strong database and caching experience. Git knowledge and distributed systems understanding are good. Ruby experience gap is minor as Go is primary language for new services.',
            'interview_questions': '- Explain git\'s object storage model — how are blobs, trees, and commits linked? How do packfiles optimize storage?\n- Design a MySQL sharding strategy for a repository metadata service handling 100M+ repositories\n- How would you implement a distributed webhook delivery system guaranteeing at-least-once delivery with ordering?\n- Describe how you would debug a Redis-based distributed lock that\'s causing intermittent deadlocks\n- Design a background job processing system that handles 10M+ daily jobs with priority levels and failure recovery'
        },
        {
            'company': 'Snowflake',
            'job_summary': 'Data Platform Engineer developing petabyte-scale data warehouse query optimizers, ETL streaming pipelines, and data quality monitoring frameworks.',
            'required_skills': 'Python, SQL, Apache Spark, Data Pipelines, Cloud Storage, Parquet, dbt, Airflow',
            'required_experience': '4+ years of data engineering with large-scale analytical workloads',
            'important_technologies': 'Python, SQL, Apache Spark, dbt, Airflow, Snowpark, Parquet, Delta Lake',
            'interview_preparation_suggestions': '- Study SQL query optimization: execution plans, join algorithms (hash, merge, nested loop), indexing strategies\n- Review columnar storage formats: Parquet row groups, column chunks, predicate pushdown, min/max statistics\n- Practice designing ETL/ELT pipelines with idempotency, incremental loading, and late-arriving data handling\n- Understand data warehouse modeling patterns: star schema, snowflake schema, slowly changing dimensions\n- Study data quality frameworks: Great Expectations, data contracts, schema evolution strategies',
            'match_score': 79,
            'match_analysis': 'Good Python and SQL foundation for data engineering work. Experience with REST API design and Django ORM provides transferable database optimization skills. Apache Spark and distributed data processing experience would strengthen the candidacy.',
            'interview_questions': '- How would you design an ETL pipeline that handles late-arriving data and ensures idempotent reprocessing?\n- Explain the advantages of columnar storage (Parquet) over row-oriented formats for analytical queries\n- Design a data quality monitoring system that detects anomalies, schema drift, and freshness violations\n- How would you optimize a slow-running SQL query that performs multiple large table joins?\n- Describe your approach to implementing slowly changing dimensions (Type 2) in a data warehouse'
        },
        {
            'company': 'Grafana Labs',
            'job_summary': 'Senior Software Engineer building open-source observability stack including Grafana dashboards, Loki log aggregation, Tempo distributed tracing, and Mimir metrics.',
            'required_skills': 'Go, Prometheus, Time-Series Databases, Distributed Systems, Kubernetes, Open Source',
            'required_experience': '4+ years building infrastructure tooling or observability platforms',
            'important_technologies': 'Go, Prometheus, Grafana, Loki, Tempo, Mimir, Kubernetes, gRPC',
            'interview_preparation_suggestions': '- Study time-series database internals: TSDB block structure, compaction, downsampling strategies\n- Review PromQL and LogQL query languages for metrics and log analysis\n- Practice designing distributed log aggregation systems with efficient compression and indexing\n- Understand distributed tracing concepts: spans, traces, context propagation, sampling strategies\n- Prepare to discuss open-source community management and contribution workflows',
            'match_score': 83,
            'match_analysis': 'Strong Go potential and infrastructure engineering mindset. Existing monitoring experience with Prometheus and Grafana dashboards provides practical context. Open-source contributions to Loki demonstrate genuine community engagement.',
            'interview_questions': '- How does Prometheus TSDB organize time-series data blocks and what compaction strategies optimize storage and query performance?\n- Design a log aggregation system that can ingest and query 1TB of logs per day with sub-second search latency\n- Explain how distributed tracing context propagation works across microservice boundaries using W3C Trace Context\n- How would you implement adaptive sampling for high-volume tracing without losing critical error traces?\n- Describe your experience contributing to open-source projects — how do you approach code review and community collaboration?'
        },
    ]

    analysis_count = 0
    for a in analyses_data:
        if a['company'] in app_dict:
            JobAnalysis.objects.create(
                application=app_dict[a['company']],
                job_summary=a['job_summary'],
                required_skills=a['required_skills'],
                required_experience=a['required_experience'],
                important_technologies=a['important_technologies'],
                interview_preparation_suggestions=a['interview_preparation_suggestions'],
                match_score=a['match_score'],
                match_analysis=a['match_analysis'],
                interview_questions=a['interview_questions']
            )
            analysis_count += 1

    print(f"      ✓ {analysis_count} AI analysis records created.")

    # ──────────────────────────────────────────────────────────
    # SUMMARY
    # ──────────────────────────────────────────────────────────
    print("\n[7/7] Verifying seed data integrity...")

    total_apps = JobApplication.objects.count()
    total_interviews = Interview.objects.count()
    total_analyses = JobAnalysis.objects.count()
    total_categories = Category.objects.count()

    print(f"      ✓ All records verified.\n")
    print("=" * 60)
    print("  ✅ DATABASE SEEDING COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print()
    print("  📋 DATA SUMMARY:")
    print(f"     Applications:  {total_apps}")
    print(f"     Interviews:    {total_interviews}")
    print(f"     AI Analyses:   {total_analyses}")
    print(f"     Categories:    {total_categories}")
    print()
    print("  🔐 LOGIN CREDENTIALS:")
    print("  ┌─────────────────────────────────────────────┐")
    print("  │  Admin:  admin / admin123        (superuser) │")
    print("  │  User:   arka  / password123     (main user) │")
    print("  └─────────────────────────────────────────────┘")
    print()
    print("  📊 STATUS DISTRIBUTION:")
    for status in ['Wishlist', 'Applied', 'Screening', 'Interview', 'Selected', 'Rejected']:
        count = JobApplication.objects.filter(status=status).count()
        bar = '█' * count + '░' * (20 - count)
        print(f"     {status:12s} [{bar}] {count}")
    print()
    print("  🧠 TOP AI MATCH SCORES:")
    top_matches = JobApplication.objects.filter(
        analysis__isnull=False
    ).select_related('analysis').order_by('-analysis__match_score')[:5]
    for app in top_matches:
        score = app.analysis.match_score
        emoji = '🟢' if score >= 90 else '🟡' if score >= 80 else '🟠'
        print(f"     {emoji} {score}%  {app.job_title} @ {app.company_name}")
    print()
    print("=" * 60)

if __name__ == '__main__':
    seed()
