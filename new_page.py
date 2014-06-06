import sublime, sublime_plugin
import os, time

class ManPageNewCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
            os.path.join(sublime.packages_path(), 'User'))
        v.set_syntax_file('Packages/sublime_man_page_support/man-groff.tmLanguage')

        template = """.\" Manpage for ${1:<COMMAND>}.
.\" Contact ${2:<AUTHOR_EMAIL>} to correct errors or typos.
.TH man 8 "%s" "1.0" "${1:<COMMAND>}"
.SH NAME
${1:<COMMAND>}
.SH SYNOPSIS
.SY
${1:<COMMAND>}
.YS
.SH DESCRIPTION
${1:<COMMAND>}
.SH BUGS
No known bugs.
.SH SEE ALSO
.SH AUTHOR
.MT ${2:<AUTHOR_EMAIL>}
${3:<AUTHOR_NAME>}
.ME
""" %(time.strftime("%B %Y"))
        v.run_command("insert_snippet", {"contents": template})
