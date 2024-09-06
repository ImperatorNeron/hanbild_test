from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from main.views import BaseApplicationFormView
from solution.models import Solution, SolutionPhotos, SolutionVideos


class SolutionView(BaseApplicationFormView):
    template_name = "solution/solutions.html"
    success_url = reverse_lazy("solution:solution")
    title = _(
        "Послуги HanBild: виробництво та обслуговування причепів та напівпричепів"
    )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["solutions"] = Solution.objects.filter()
        return context


class SolutionPageView(BaseApplicationFormView):
    template_name = "solution/solution_page.html"
    success_url = reverse_lazy("solution:solution_page")

    def get(self, request, slug, *args, **kwargs):
        solution = get_object_or_404(Solution, slug=slug)
        solution_photos = SolutionPhotos.objects.filter(solution=solution)
        solution_videos = SolutionVideos.objects.filter(solution=solution)

        return render(
            request,
            self.template_name,
            {
                "solution": solution,
                "solution_photos": solution_photos,
                "solution_videos": solution_videos,
            },
        )

    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse_lazy(
            "solution:solution_page",
            kwargs={
                "slug": kwargs["slug"],
            },
        )
        return super().dispatch(request, *args, **kwargs)

