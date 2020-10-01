from fpdf import FPDF
import os

temp_destination = '/Users/jennacampbell/Desktop'

def create_pdf(name, orientation, gender, speed, fig1_dest, fig2_dest, fig3_dest, destination=temp_destination):

    pdf = FPDF()
    pdf.add_page()  
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(r=0,g=40,b=70)
    pdf.ln()
    pdf.ln()

    title = "Dolphin Kick Analysis for {name}".format(name=name)
    pdf.cell(0, 8, title, 0, 1,'C')

    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(r=60,g=60,b=60)
    gender_text = "Gender: {gender}".format(gender=gender)
    orientation_text = "Orientation: {orientation}".format(orientation=orientation)
    speed_text = "Speed: {speed}".format(speed=speed)
    subtitle = gender_text +"       "+orientation_text+"      "+speed_text
    pdf.cell(0,8,subtitle,0,1,'C')
    pdf.ln()

    pdf.set_font('Arial','',11)
    pdf.set_text_color(r=50,g=50,b=50)
    graph1_title = 'Vertical Variation Over Time'
    graph3_title = 'Time Decomposition'
    pdf.cell(90,8,graph1_title,0,0,'C')
    pdf.cell(120,8,graph3_title,0,1,'C')

    pdf.image(fig1_dest, x=7, y=42, h=70)
    pdf.image(fig3_dest, x=102, y=42, h=66)

    pdf.set_xy(x=25,y=110)
    pdf.set_font('Arial','',7)
    pdf.set_text_color(r=0,g=0,b=0)
    graph3_explanation = 'Time interval between key points of kick. See below for definitions of key points'
    graph1_explanation = 'All displacement values calculated relative to hip'
    pdf.cell(50,8,graph1_explanation,0,0,'C')
    pdf.cell(127,8,graph3_explanation,0,1,'R')
    

    graph2_title = 'Statistical Analysis of Vertical Displacement'
    graph2_subtitle = 'Figure shows comparison of vertical displacement of key joints on swimmers body with average vertical displacement of key joints from professional swimmers during four distinct time points within the kick. All statistically significant differences are marked red.'
    pdf.set_xy(x=10,y=123)
    pdf.set_font('Arial','',13)
    pdf.set_text_color(r=50,g=50,b=50)
    pdf.cell(0,8, graph2_title,0,1,'C')
    pdf.set_font('Arial','',9)
    pdf.set_text_color(r=0,g=0,b=0)

    pdf.image(fig2_dest,x=15, y=130, w=190)
    pdf.set_xy(x=20,y=255)
    pdf.multi_cell(0,5, graph2_subtitle,0,1,'C')

    file_name = name + "_dolphinkickanalyis"'.pdf'
    save_path = os.path.join(destination, file_name)

    pdf.output(save_path, 'F')

    return pdf