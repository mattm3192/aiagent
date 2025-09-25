import os


def get_file_content(working_directory, file_path):
	abs_working_dir = os.path.abspath(working_directory)
	target_file = os.path.abspath(os.path.join(working_directory, file_path))
	if not target_file.startswith(abs_working_dir):
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
	
	if not os.path.isfile(target_file):
		return f'Error: File not found or is not a regular file: "{file_path}"'
	MAX_CHARS = 10000
	try:
		file_content = []
		with open(target_file, "r") as f:
			file_content_string = f.read(MAX_CHARS)
		file_content.append(file_content_string)
		if len(file_content_string) == MAX_CHARS:
			file_content.append(f'[...File "{file_path}" truncated at 10000 characters]')
		return " ".join(file_content)
	except Exception as e:
		return f'Error reading file "{file_path}": {e}'