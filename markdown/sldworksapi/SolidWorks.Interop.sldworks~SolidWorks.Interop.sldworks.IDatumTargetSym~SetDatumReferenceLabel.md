---
title: "SetDatumReferenceLabel Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "SetDatumReferenceLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumReferenceLabel.html"
---

# SetDatumReferenceLabel Method (IDatumTargetSym)

Sets the specified datum target reference label.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDatumReferenceLabel( _
   ByVal WhichOne As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim WhichOne As System.Integer
Dim Text As System.String
Dim value As System.Boolean

value = instance.SetDatumReferenceLabel(WhichOne, Text)
```

### C#

```csharp
System.bool SetDatumReferenceLabel(
   System.int WhichOne,
   System.string Text
)
```

### C++/CLI

```cpp
System.bool SetDatumReferenceLabel(
   System.int WhichOne,
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: 0-based index indicating the datum reference label to set
- `Text`: Datum reference label

### Return Value

True if the datum reference label is set successfully, false if it was not

## VBA Syntax

See [DatumTargetSym::SetDatumReferenceLabel](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~SetDatumReferenceLabel.html).

## Examples

[Insert and Modify Datum Target Symbol (C#)](Insert_and_Modify_Datum_Target_Symbol_Example_CSharp.htm)
[Insert and Modify Datum Target Symbol (VB.NET)](Insert_and_Modify_Datum_Target_Symbol_Example_VBNET.htm)
[Insert and Modify Datum Target Symbol (VBA)](Insert_and_Modify_Datum_Target_Symbol_Example_VB.htm)

## Remarks

Use [IDatumTargetSym::GetDatumReferenceLabel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetDatumReferenceLabel.html) to get the datum target reference labels.

To see the change in a drawing, call [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
