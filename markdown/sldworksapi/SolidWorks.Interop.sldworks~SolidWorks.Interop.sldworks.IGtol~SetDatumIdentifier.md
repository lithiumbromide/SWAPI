---
title: "SetDatumIdentifier Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetDatumIdentifier"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetDatumIdentifier.html"
---

# SetDatumIdentifier Method (IGtol)

Sets the name of the datum being defined.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDatumIdentifier( _
   ByVal DatumIdentifier As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim DatumIdentifier As System.String

instance.SetDatumIdentifier(DatumIdentifier)
```

### C#

```csharp
void SetDatumIdentifier(
   System.string DatumIdentifier
)
```

### C++/CLI

```cpp
void SetDatumIdentifier(
   System.String^ DatumIdentifier
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DatumIdentifier`: Name of datum

## VBA Syntax

See [Gtol::SetDatumIdentifier](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetDatumIdentifier.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetDatumIdentifier Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetDatumIdentifier.html)
