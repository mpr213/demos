import os
import sys
import zipfile

from zipfile import ZIP_DEFLATED


def makedirs_if_missing(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def make_zip(root, dest, assignment_id):
    with zipfile.ZipFile(dest, 'w', ZIP_DEFLATED) as zfh:
        for path, _, files in os.walk(root):
            for f in files:
                filename = os.path.join(path, f)
                arcname = os.path.join(
                    assignment_id, os.path.relpath(filename, root))
                zfh.write(filename, arcname)


def main(assignment_id):
    root = os.getcwd()
    feedback_dir = os.path.join(root, 'feedback')
    dest_dir = os.path.join(root, 'uploaded', 'feedback', assignment_id)
    makedirs_if_missing(dest_dir)

    for student in sorted(os.listdir(feedback_dir)):
        assignment_dir = os.path.join(feedback_dir, student, assignment_id)
        if os.path.exists(assignment_dir):
            print("Zipping student feedback: feedback/{}/{}".format(
                student, assignment_id))
            dest = os.path.join(dest_dir, "{}.zip".format(student))
            make_zip(assignment_dir, dest, assignment_id)


if __name__ == "__main__":
    extra_args = sys.argv[1:]
    if len(extra_args) > 1:
        print("Only one argument (the assignment id) may be specified")
        sys.exit(1)
    elif len(extra_args) == 0:
        print("An assignment id must be specified")
        sys.exit(1)
    else:
        main(extra_args[0])
