from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, reverse


class LoggedOutOnlyView(UserPassesTestMixin):

    # LoggedOutOnlyView 를 뷰 안에 놓을 때마다 test_function 을 부르게 됨.
    # test_func. 은 true 를 return 해야만 함.
    # 아래 코드에서의 return true 는 '유저는 인증이 되지 않음'을 의미함. 익명의 유저.
    def test_func(self):
        return not self.request.user.is_authenticated

    # 이 mixin view 를 다른 view 앞에 추가해 주면
    # test_func 이 return false 일 경우 home 으로 redirect
    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect(reverse("core:home"))
