import cgi, cgitb
cgitb.enable()
frm=cgi.FieldStorage()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Registration</title>
</head>
<body>
<h2>Basic Calculator</h2>
<form name="cal_frm" method="post">
    <table cellpadding="10">
        <tr>
            <td>Enter 1st Number</td>
            <td><input type="text" name="n1" required></td>
        </tr>
        <tr>
            <td>Select Operation</td>
            <td>
                <select name="ope">
                    <option value="add">+</option>
                    <option value="sub">-</option>
                    <option value="mult">*</option>
                    <option value="div">/</option>
                    <option value="" selected>-Select Operation-</option>
                </select>
            </td>
        </tr>
        <tr>
            <td>Enter 2nd Number</td>
            <td><input type="text" name="n2" required></td>
        </tr>
        <tr>
            <td colspan="2" align="center">
                <input type="submit" name="ok" value="Get Result">
            </td>
        </tr>
    </table>
</form>''')
if frm.getvalue('ok'):
    n1=int(frm.getvalue('n1'))
    n2=int(frm.getvalue('n2'))
    ope=frm.getvalue('ope')
    if ope=='add':
        res=n1+n2
        print("The Addition is {}".format(res))
    elif ope=='sub':
        res = n1 - n2
        print("The Subtraction is {}".format(res))
    elif ope=='mult':
        res = n1 * n2
        print("The Multipication is {}".format(res))
    elif ope=='div':
        res = n1 / n2
        print("The Division is {}".format(res))
    else:
        print('Please select an opertation')
print('''</body>
</html>''')
print('Thankyou')
