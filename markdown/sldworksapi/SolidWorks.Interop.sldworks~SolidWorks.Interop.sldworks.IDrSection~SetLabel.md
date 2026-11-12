---
title: "SetLabel Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLabel.html"
---

# SetLabel Method (IDrSection)

Obsolete. Superseded by [IDrSection::ISetLabel2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~SetLabel2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLabel( _
   ByVal Label As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
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

- `Label`:

## VBA Syntax

See [DrSection::SetLabel](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetLabel.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
