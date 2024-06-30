$ExeIcon:'Logo.ico'
Screen _NewImage(1, 1, 32)
ui0& = _LoadImage("UI\UI0.jpg")
ui1& = _LoadImage("UI\UI1.jpg")
ui2& = _LoadImage("UI\UI2.jpg")
ui3& = _LoadImage("UI\UI3.jpg")
ui4& = _LoadImage("UI\UI4.jpg")
ui5& = _LoadImage("UI\UI5.jpg")
ui6& = _LoadImage("UI\UI6.jpg")
ui7& = _LoadImage("UI\UI7.jpg")
ui8& = _LoadImage("UI\UI8.jpg")
ui9& = _LoadImage("UI\UI9.jpg")
UI10& = _LoadImage("UI\UI10.jpg")
UI11& = _LoadImage("UI\UI11.jpg")
UI12& = _LoadImage("UI\UI12.jpg")
UI13& = _LoadImage("UI\UI13.jpg")
UI14& = _LoadImage("UI\UI14.jpg")
UI15& = _LoadImage("UI\UI15.jpg")
UI16& = _LoadImage("UI\UI16.jpg")
UI17& = _LoadImage("UI\UI17.jpg")
UI18& = _LoadImage("UI\UI18.jpg")
UI19& = _LoadImage("UI\UI19.jpg")
UI20& = _LoadImage("UI\UI20.jpg")
UI21& = _LoadImage("UI\UI21.jpg")
UI22& = _LoadImage("UI\UI22.jpg")
UI23& = _LoadImage("UI\UI23.jpg")

Screen _NewImage(1280, 720, 32)
_Title ("Cryptify")

start:
Do
    While _MouseInput
        X = _MouseX
        Y = _MouseY
        If (X > 100 And X < 498 And Y > 138 And Y < 220) Then
            Screen ui1&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button1
        ElseIf (X > 100 And X < 498 And Y > 257 And Y < 339) Then
            Screen ui2&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button2
        ElseIf (X > 100 And X < 498 And Y > 377 And Y < 458) Then
            Screen ui3&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button3
        ElseIf (X > 100 And X < 498 And Y > 498 And Y < 577) Then
            Screen ui4&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button4

        ElseIf (X > 779 And X < 1176 And Y > 138 And Y < 220) Then
            Screen ui5&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button5
        ElseIf (X > 779 And X < 1176 And Y > 257 And Y < 339) Then
            Screen ui6&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button6
        ElseIf (X > 779 And X < 1176 And Y > 377 And Y < 458) Then
            Screen ui7&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button7
        ElseIf (X > 779 And X < 1176 And Y > 498 And Y < 577) Then
            Screen ui8&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button8

        ElseIf (X > 128 And X < 361 And Y > 616 And Y < 675) Then
            Screen ui9&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button9
        ElseIf (X > 525 And X < 757 And Y > 616 And Y < 675) Then
            Screen UI10&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: System
        ElseIf (X > 912 And X < 1145 And Y > 616 And Y < 675) Then
            Screen UI11&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo button10

        ElseIf (X > 594 And X < 706 And Y > 33 And Y < 178) Then
            Screen UI12&
            If (_MouseButton(1) = -1) Then Call ClearBuffer

        Else
            Screen ui0&
        End If
    Wend
Loop

button1:
Shell _Hide ("start menu.exe 1")
GoTo start
button2:
Shell _Hide ("start menu.exe 2")
GoTo start
button3:
Shell _Hide ("start menu.exe 3")
GoTo start
button4:
Shell _Hide ("start menu.exe 4")
GoTo start
button5:
Shell _Hide ("start menu.exe 5")
GoTo start
button6:
Shell _Hide ("start menu.exe 6")
GoTo start
button7:
Shell _Hide ("start menu.exe 7")
GoTo start
button8:
Shell _Hide ("start menu.exe 8")
GoTo start
button9:
Do
    While _MouseInput
        X = _MouseX
        Y = _MouseY
        If (X > 399 And X < 600 And Y > 329 And Y < 360) Then
            Screen UI14&
        ElseIf (X > 232 And X < 495 And Y > 493 And Y < 516) Then
            Screen UI15&
        ElseIf (X > 232 And X < 532 And Y > 532 And Y < 560) Then
            Screen UI16&
        ElseIf (X > 232 And X < 460 And Y > 577 And Y < 600) Then
            Screen UI17&
        ElseIf (X > 232 And X < 417 And Y > 618 And Y < 649) Then
            Screen UI18&
        ElseIf (X > 970 And X < 1202 And Y > 597 And Y < 658) Then
            Screen UI19&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo start
        Else
            Screen UI13&
        End If
    Wend
Loop

button10:
Do
    While _MouseInput
        X = _MouseX
        Y = _MouseY
        If (X > 172 And X < 470 And Y > 597 And Y < 658) Then
            Screen UI21&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: Shell _Hide ("python newface.pyc")
        ElseIf (X > 510 And X < 925 And Y > 597 And Y < 658) Then
            Screen UI22&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: Shell _Hide ("start req.exe")
        ElseIf (X > 970 And X < 1202 And Y > 597 And Y < 658) Then
            Screen UI23&
            If (_MouseButton(1) = -1) Then Call ClearBuffer: GoTo start
        Else
            Screen UI20&
        End If
    Wend
Loop

Sub ClearBuffer
    Do
        i = _MouseInput
        b = _MouseButton(1)
    Loop Until b = 0
End Sub


