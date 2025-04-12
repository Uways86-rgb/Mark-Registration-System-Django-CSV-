from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import csv
import os
from django.contrib import messages
import logging

# Configure logging
logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        num_students = request.POST.get('num_students')
        num_modules = request.POST.get('num_modules')

        # Save input data to CSV
        output_file_path = r"C:\Users\User 1\Website\Records.csv"  # Update the path to the "Website" directory
        try:
            with open(output_file_path, 'a', newline='', encoding='utf-8') as output_file:
                fieldnames = ["num_students", "num_modules"]
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                if output_file.tell() == 0:
                    writer.writeheader()
                writer.writerow({
                    "num_students": num_students,
                    "num_modules": num_modules
                })
            logger.info(f"CSV file updated successfully at {output_file_path}")
            messages.success(request, "Records saved successfully.")
        except Exception as e:
            logger.error(f"Error writing CSV file: {e}")
            messages.error(request, f"Error writing CSV file: {e}")

        return redirect('index')

    return render(request, 'marks/home.html')

def input_marks(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        module_code = request.POST.get('module_code')
        classwork1 = request.POST.get('classwork1')
        classwork2 = request.POST.get('classwork2')
        classwork3 = request.POST.get('classwork3')

        # Save input data to CSV
        output_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Update the path to the "Website" directory
        try:
            with open(output_file_path, 'a', newline='', encoding='utf-8') as output_file:
                fieldnames = ["student_id", "student_name", "module_code", "classwork1", "classwork2", "classwork3"]
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                if output_file.tell() == 0:
                    writer.writeheader()
                writer.writerow({
                    "student_id": student_id,
                    "student_name": student_name,
                    "module_code": module_code,
                    "classwork1": classwork1,
                    "classwork2": classwork2,
                    "classwork3": classwork3
                })
            logger.info(f"CSV file updated successfully at {output_file_path}")
        except Exception as e:
            logger.error(f"Error writing CSV file: {e}")
            messages.error(request, f"Error writing CSV file: {e}")

        return redirect('view-marks')

    return render(request, 'marks/input-marks.html')

def view_marks(request):
    module_code = request.GET.get('module_code', None)
    data = []
    input_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Update the path to the "Website" directory

    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                if row['module_code'] == module_code:
                    row['total'] = int(row['classwork1']) + int(row['classwork2']) + int(row['classwork3'])
                    data.append(row)
                elif module_code is None or module_code == '':
                    module_code = request.GET.get('module_code', '')
                    row['total'] = int(row['classwork1']) + int(row['classwork2']) + int(row['classwork3'])
                    data.append(row)
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        messages.error(request, f"Error reading CSV file: {e}")

    return render(request, 'marks/view-marks.html', {'marks': data, 'module_code': module_code})

def update_marks(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        module_code = request.POST.get('module_code')
        classwork1 = request.POST.get('classwork1')
        classwork2 = request.POST.get('classwork2')
        classwork3 = request.POST.get('classwork3')

        input_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Update the path to the "Website" directory
        temp_file_path = r"C:\Users\User 1\Website\Temp_Input_Marks.csv"  # Temporary file path in the "Website" directory

        try:
            with open(input_file_path, 'r', encoding='utf-8') as input_file, open(temp_file_path, 'w', newline='', encoding='utf-8') as temp_file:
                reader = csv.DictReader(input_file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row['student_id'] == student_id and row['module_code'] == module_code:
                        row['student_name'] = student_name
                        row['classwork1'] = classwork1
                        row['classwork2'] = classwork2
                        row['classwork3'] = classwork3
                    writer.writerow(row)
            os.replace(temp_file_path, input_file_path)
            logger.info(f"CSV file updated successfully at {input_file_path}")
        except Exception as e:
            logger.error(f"Error updating CSV file: {e}")
            messages.error(request, f"Error updating CSV file: {e}")

        return redirect('view-marks')
    else:
        student_id = request.GET.get('student_id')
        module_code = request.GET.get('module_code')
        student_name = request.GET.get('student_name')
        classwork1 = request.GET.get('classwork1')
        classwork2 = request.GET.get('classwork2')
        classwork3 = request.GET.get('classwork3')
        input_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Update the path to the "Website" directory
        return render(request, 'marks/update-marks.html', {'student_id': student_id, 'module_code': module_code, 'student_name': student_name, 'classwork1': classwork1, 'classwork2': classwork2, 'classwork3': classwork3})

def visualisation(request):
    return render(request, 'marks/visualisation.html')

def chart_data(request):
    data = []
    input_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Update the path to the "Website" directory

    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            reader = csv.DictReader(input_file)
            module_totals = {}
            for row in reader:
                print(row)
                module_code = row['module_code']
                total = int(row['classwork1']) + int(row['classwork2']) + int(row['classwork3'])
                if module_code in module_totals:
                    module_totals[module_code] += total
                else:
                    module_totals[module_code] = total
            data = {
                'labels': list(module_totals.keys()),
                'values': list(module_totals.values())
            }

    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return JsonResponse({'error': f"Error reading CSV file: {e}"}, status=500)
    print(data)
    return JsonResponse(data)



def chart_data_student(request):
    module_code_param = request.GET.get('module_code')  # Récupère le module_code depuis les paramètres de requête
    data = []
    input_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Mettre à jour le chemin
    
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            reader = csv.DictReader(input_file)
            students = []
            for row in reader:
                if row['module_code'] == module_code_param:
                    total = int(row['classwork1']) + int(row['classwork2']) + int(row['classwork3'])
                    students.append({
                        'student_id': row['student_id'],
                        'student_name': row['student_name'],
                        'total_marks': total
                    })
            
            data = {'students': students}
    
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return JsonResponse({'error': f"Error reading CSV file: {e}"}, status=500)
    
    return JsonResponse(data)



def delete_marks(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        module_code = request.POST.get('module_code')

        input_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Update the path to the "Website" directory
        temp_file_path = r"C:\Users\User 1\Website\Temp_Input_Marks.csv"  # Temporary file path in the "Website" directory

        try:
            with open(input_file_path, 'r', encoding='utf-8') as input_file, open(temp_file_path, 'w', newline='', encoding='utf-8') as temp_file:
                reader = csv.DictReader(input_file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row['student_id'] == student_id and row['module_code'] == module_code:
                        continue
                    writer.writerow(row)
            os.replace(temp_file_path, input_file_path)
            logger.info(f"CSV file updated successfully at {input_file_path}")
        except Exception as e:
            logger.error(f"Error updating CSV file: {e}")
            messages.error(request, f"Error updating CSV file: {e}")

        return redirect('view-marks')

    return redirect('view-marks')

def show_one_record(request):
    student_id = request.GET.get('student_id')
    module_code = request.GET.get('module_code')
    data = []
    input_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Update the path to the "Website" directory

    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                if row['student_id'] == student_id and row['module_code'] == module_code:
                    row['total'] = int(row['classwork1']) + int(row['classwork2']) + int(row['classwork3'])
                    data.append(row)
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        messages.error(request, f"Error reading CSV file: {e}")

    return render(request, 'marks/view-marks.html', {'marks': data, 'module_code': module_code})


def export_database_to_csv(request):
    input_file_path = r"C:\Users\User 1\Website\Input_Marks.csv"  # Update the path to the "Website" directory

    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            reader = csv.DictReader(input_file)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Database_Marks.csv"'
            writer = csv.DictWriter(response, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                writer.writerow(row)
            logger.info("CSV file exported successfully")
            return response
    except Exception as e:
        logger.error(f"Error exporting CSV file: {e}")
        messages.error(request, f"Error exporting CSV file: {e}")
        return redirect('view-marks')