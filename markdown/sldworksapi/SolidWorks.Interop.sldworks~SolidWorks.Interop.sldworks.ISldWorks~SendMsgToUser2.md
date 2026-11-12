---
title: "SendMsgToUser2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SendMsgToUser2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SendMsgToUser2.html"
---

# SendMsgToUser2 Method (ISldWorks)

Displays a message box containing a message to the user, who is required to interact with it before continuing.

## Syntax

### Visual Basic (Declaration)

```vb
Function SendMsgToUser2( _
   ByVal Message As System.String, _
   ByVal Icon As System.Integer, _
   ByVal Buttons As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Message As System.String
Dim Icon As System.Integer
Dim Buttons As System.Integer
Dim value As System.Integer

value = instance.SendMsgToUser2(Message, Icon, Buttons)
```

### C#

```csharp
System.int SendMsgToUser2(
   System.string Message,
   System.int Icon,
   System.int Buttons
)
```

### C++/CLI

```cpp
System.int SendMsgToUser2(
   System.String^ Message,
   System.int Icon,
   System.int Buttons
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Message`: Message for user
- `Icon`: Icon to show in the message box as defined in [swMessageBoxIcon_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxIcon_e.html)
- `Buttons`: Buttons to show in the message box as defined in [swMessageBoxBtn_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxBtn_e.html)

### Return Value

Value corresponding to the button the user clicked as defined in [swMessageBoxResult_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxResult_e.html)

## VBA Syntax

See [SldWorks::SendMsgToUser2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SendMsgToUser2.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Detecting In-context Edit (C++)](Get_Edit_In_Context_Example_CPlusPlus_COM.htm)
[Access Selections (VBA)](Access_Selections_Example_VB.htm)
[Save Drawing As DXF (VBA)](Save_Drawing_as_DXF_Example_VB.htm)
[Save Drawing as DXF (VB.NET)](Save_Drawing_as_DXF_Example_VBNET.htm)
[Save Drawing as DXF (C#)](Save_Drawing_as_DXF_Example_CSharp.htm)
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
