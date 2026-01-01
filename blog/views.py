from django.shortcuts import render

blogs = [
    {
        "id": 1,
        "title": "Building Scalable Web Applications in 2025",
        "description": (
            "Modern web applications are expected to handle rapid growth, high traffic, "
            "and evolving feature requirements. Scalability must be designed from day one. "
            "A strong architecture with clear separation between frontend, backend, and "
            "database layers enables teams to scale efficiently while maintaining performance "
            "and code quality."
        ),
        "category": "Web Development",
        "publish_date": "2025-01-10",
        "image": "blog/images/scale_web_apps.png",
    },
    {
        "id": 2,
        "title": "Why UI/UX Design Matters More Than Ever",
        "description": (
            "In a competitive digital landscape, users expect clarity, simplicity, and "
            "accessibility. UI/UX design directly impacts user trust, engagement, and "
            "retention by focusing on intuitive navigation, consistent layouts, and "
            "problem-solving design principles."
        ),
        "category": "Design & UX",
        "publish_date": "2025-02-02",
        "image": "blog/images/design.jpg",
    },
    {
        "id": 3,
        "title": "The Rise of Automation in Digital Products",
        "description": (
            "Automation is reshaping how digital products are built and scaled. From "
            "automated testing to AI-powered workflows, automation improves consistency, "
            "reduces manual effort, and allows teams to focus on high-impact work such as "
            "innovation and user experience."
        ),
        "category": "Technology",
        "publish_date": "2025-03-05",
        "image": "blog/images/automation.png",
    },
]


def homepage(request):
    return render(request, "blog/homepage.html", {"blogs": blogs})


def posts(request):
    return render(request, "blog/all-posts.html", {"blogs": blogs})


def post_detail(request):
    pass
