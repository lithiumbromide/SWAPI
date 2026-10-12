---
title: "SetLabel Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "SetLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetLabel.html"
---

# SetLabel Method (IDatumTag)

Sets the label for this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLabel( _
   ByVal Label As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim Label As System.String
Dim value As System.Boolean

value = instance.SetLabel(Label)
```

### C#

```csharp
System.bool SetLabel(
   System.string Label
)
```

### C++/CLI

```cpp
System.bool SetLabel(
   System.String^ Label
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Label`: Text string

### Return Value

True if the label was successfully set, false if not

## VBA Syntax

See [DatumTag::SetLabel](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~SetLabel.html).

## Remarks

The label can consist of up to two characters. If the specified label is more than two characters long, SOLIDWORKS does not change the symbol and returns false.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetLabel.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
