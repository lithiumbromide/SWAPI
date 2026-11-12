---
title: "GetLabel Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetLabel.html"
---

# GetLabel Method (IDatumTag)

Gets the label for this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLabel() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.String

value = instance.GetLabel()
```

### C#

```csharp
System.string GetLabel()
```

### C++/CLI

```cpp
System.String^ GetLabel();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Text string

## VBA Syntax

See [DatumTag::GetLabel](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetLabel.html).

## Examples

[Set Text in Datum Tags and GTols (C#)](Set_Text_in_Datum_Tags_and_GTols_Example_CSharp.htm)
[Set Text in Datum Tags and GTols (VB.NET)](Set_Text_in_Datum_Tags_and_GTols_Example_VBNET.htm)
[Set Text in Datum Tags and GTols (VBA)](Set_Text_in_Datum_Tags_and_GTols_Example_VB.htm)

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::SetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetLabel.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
