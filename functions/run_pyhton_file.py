import os, subprocess, sys


def run_python_file(working_directory, file_path, args=[]):
	abs_working_dir = os.path.abspath(working_directory)
	target_program = os.path.abspath(os.path.join(working_directory, file_path))
	
	if not target_program.startswith(abs_working_dir):
		return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
	
	if not os.path.exists(target_program):
		return f'Error: File "{file_path}" not found.'
	
	if not target_program.endswith(".py"):
		return f'Error: "{file_path}" is not a Python file.'
	
	args=[str(a) for a in args]
	cmd = [sys.executable, target_program] + args
	try:
		process_result = subprocess.run(cmd, cwd=abs_working_dir, capture_output=True, timeout=30,text=True)
		output_lines = [f"STDOUT: {process_result.stdout}", f"STDERR: {process_result.stderr}"]
		
		if len(process_result.stdout) == 0 and len(process_result.stderr) == 0:
			return "No output produced."
		
		elif process_result.returncode != 0:
			output_lines.append(f"Process exited with code {process_result.returncode}")
		
		return "\n".join(output_lines)
	
	
	except Exception as e:
		return f"Error: executing Python file: {e}"