---
title: "GetDatumReferenceLabel Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetDatumReferenceLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDatumReferenceLabel.html"
---

# GetDatumReferenceLabel Method (IDatumTargetSym)

Gets the specified datum target reference label.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumReferenceLabel( _
   ByVal WhichOne As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim WhichOne As System.Integer
Dim value As System.String

value = instance.GetDatumReferenceLabel(WhichOne)
```

### C#

```csharp
System.string GetDatumReferenceLabel(
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.String^ GetDatumReferenceLabel(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: 0-based index indicating the datum reference label to get

### Return Value

Datum reference label

## VBA Syntax

See [DatumTargetSym::GetDatumReferenceLabel](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetDatumReferenceLabel.html).

## Examples

[Insert and Modify Datum Target Symbol (C#)](Insert_and_Modify_Datum_Target_Symbol_Example_CSharp.htm)
[Insert and Modify Datum Target Symbol (VB.NET)](Insert_and_Modify_Datum_Target_Symbol_Example_VBNET.htm)
[Insert and Modify Datum Target Symbol (VBA)](Insert_and_Modify_Datum_Target_Symbol_Example_VB.htm)

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::SetDatumReferenceLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumReferenceLabel.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
