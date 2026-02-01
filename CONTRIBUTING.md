---
editor: 
  markdown: 
    wrap: 72
---

# Contributing

Contributions of all kinds are welcome here, and they are greatly
appreciated! Every little bit helps, and credit will always be given.

## Example Contributions

You can contribute in many ways, for example:

-   [Report bugs](#report-bugs)
-   [Fix Bugs](#fix-bugs)
-   [Implement Features](#implement-features)
-   [Write Documentation](#write-documentation)
-   [Submit Feedback](#submit-feedback)

### Report Bugs {#report-bugs}

Report bugs at https://github.com/UBC-MDS/datajanitor/issues.

**If you are reporting a bug, please follow the template guidelines. The
more detailed your report, the easier and thus faster we can help you.**

### Fix Bugs {#fix-bugs}

Look through the GitHub issues for bugs. Anything labelled with `bug`
and `help wanted` is open to whoever wants to implement it. When you
decide to work on such an issue, please assign yourself to it and add a
comment that you'll be working on that, too. If you see another issue
without the `help wanted` label, just post a comment, the maintainers
are usually happy for any support that they can get.

### Implement Features {#implement-features}

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement
it. As for [fixing bugs](#fix-bugs), please assign yourself to the issue
and add a comment that you'll be working on that, too. If another
enhancement catches your fancy, but it doesn't have the `help wanted`
label, just post a comment, the maintainers are usually happy for any
support that they can get.

### Write Documentation {#write-documentation}

datajanitor could always use more documentation, whether as part of the
official documentation, in docstrings, or even on the web in blog posts,
articles, and such. Just [open an
issue](https://github.com/UBC-MDS/datajanitor/issues) to let us know
what you will be working on so that we can provide you with guidance.

### Submit Feedback {#submit-feedback}

The best way to send feedback is to file an issue at
https://github.com/UBC-MDS/datajanitor/issues. If your feedback fits the
format of one of the issue templates, please use that. Remember that
this is a volunteer-driven project and everybody has limited time.

## Get Started!

Ready to contribute? Here's how to set up datajanitor for local
development.

1.  Fork the https://github.com/UBC-MDS/datajanitor repository on
    GitHub.

2.  Clone your fork locally (*if you want to work locally*)

    ``` shell
    git clone git@github.com:your_name_here/datajanitor.git
    ```

3.  [Install hatch](https://hatch.pypa.io/latest/install/).

4.  Create a branch for local development using the default branch
    (typically `main`) as a starting point. Use `fix` or `feat` as a
    prefix for your branch name.

    ``` shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.

5.  When you're done making changes, apply the quality assurance tools
    and check that your changes pass our test suite. This is all
    included with tox

    ``` shell
    hatch run test:run
    ```

6.  Commit your changes and push your branch to GitHub. Please use
    [semantic commit messages](https://www.conventionalcommits.org/).

    ``` shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7.  Open the link displayed in the message when pushing your new branch
    in order to submit a pull request.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring.
3.  Your pull request will automatically be checked by the full test
    suite. It needs to pass all of them before it can be considered for
    merging.

### Development tools and GitHub workflow

This project follows a lightweight but structured development workflow
so contributions stay reproducible, reviewable, and safe to merge. The
general approach is: keep the local setup consistent across machines,
automate code quality checks, and rely on GitHub-based guardrails to
catch issues early. A reproducible environment matters here because
small differences in dependency versions can cause tests or formatting
to behave differently across contributors’ setups. To reduce “style
discussion” during review, automated tooling is used to enforce
consistent formatting and catch common issues before code is merged.
Testing is treated as a core part of development, since data cleaning
utilities can break in subtle ways (for example, edge cases like extra
whitespace, unusual column names, empty inputs, or unexpected types).
Unit tests help protect expected behavior and make refactors safer.

On the collaboration side, contributions are organized through issues
and pull requests, with automated checks running in CI via GitHub
Actions. Issues are used to document bugs, feature requests, and design
decisions, while pull requests link changes to the relevant discussion
and provide a clear summary of what changed and how to test it. Keeping
pull requests small and focused (one fix or feature at a time) helps
reviews stay efficient and reduces merge conflicts. Overall, these
development tools, GitHub infrastructure, and organizational practices
are used to keep the codebase stable while making it easy for new
contributors to onboard and confidently contribute.
