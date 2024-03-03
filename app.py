from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_resin_hardener_ratio(total_weight, choice, sub_choice=None):
    if choice == 0:
        X = total_weight / 135
        resin = 100 * X
        hardener = 35 * X
    elif choice == 1:
        X = total_weight / 145
        resin = 100 * X
        hardener = 45 * X
    elif choice == 2:
        X = total_weight / 135
        resin = 100 * X
        hardener = 35 * X
    elif choice == 3:
        X = total_weight / 150
        resin = 100 * X
        hardener = 50 * X
    elif choice == 5:
        if sub_choice == 1:
            X = total_weight / 17
            resin = 16*X
            hardener = 1*X
        elif sub_choice == 2:
            X = total_weight / 4
            resin = 3*X
            hardener = 1*X
        elif sub_choice == 3:
            X = total_weight / 3
            resin = 2*X
            hardener = 1*X
        else:
            raise ValueError("Invalid sub-choice value")
        
        X = total_weight / (resin + hardener)
        resin = 100 * X
        hardener = 35 * X 
        
    else:
        raise ValueError("Invalid choice value")
    
    resin_amount_grams=str(round(resin, 2)) +" gms"
    hardener_amount_grams=str(round(hardener,2)) +" gms"

    return resin_amount_grams, hardener_amount_grams, total_weight


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        cloth_weight = float(request.form['cloth_weight'])
        multiplier = float(request.form['multiplier'])

        result_after_multiplier = cloth_weight * multiplier

        return render_template('result.html', result=result_after_multiplier)
    except ValueError:
        return "Error: Invalid input. Please enter valid numbers."

@app.route('/final_result', methods=['POST'])
def final_result():
    try:
        cloth_weight = float(request.form['cloth_weight'])
        multiplier = float(request.form['multiplier'])

        result_after_multiplier = cloth_weight * multiplier
        
        cloth_weight = float( request.form.get('cloth_weight'))
        material = int(request.form.get('material'))  #
        sub_choice = None
        if material == 5:
         sub_choice = int(request.form.get('resin_amount')) 
        
        resin_amount, hardener_amount, total = calculate_resin_hardener_ratio(result_after_multiplier, material, sub_choice)
        
        return render_template('final_result.html', result=result_after_multiplier, resin=resin_amount, hardener=hardener_amount, total=total)
    except ValueError:
        return "Error: Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    app.run(debug=True)
