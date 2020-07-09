This is a mock social network I created in my journey to learn Django and Python.

I originally wrote it in Django 2, but updated it for Django 3 before uploading it. This included fixing the issues with django.utils.six.

I do plan on improving this over time.

Current known issue:
- Due to an outdated package that will not work with Django 3, any user can post to any group, whether or not they're part of said group.
- Interactive background does not actually span the whole page. This is an issue with how HTML/CSS/Javascript was updated a few years ago. There's currently no fix and instead I plan to get rid of the current interactive background and make it more modern.
