---
title: "Z Property (ISelectData)"
project: "SOLIDWORKS API Help"
interface: "ISelectData"
member: "Z"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Z.html"
---

# Z Property (ISelectData)

Gets or sets the Z coordinate for the selection point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Z As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectData
Dim value As System.Double

instance.Z = value

value = instance.Z
```

### C#

```csharp
System.double Z {get; set;}
```

### C++/CLI

```cpp
property System.double Z {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Z coordinate for the selection point

## VBA Syntax

See [SelectData::Z](ms-its:sldworksapivb6.chm::/sldworks~SelectData~Z.html).

## See Also

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html)
[ISelectData::X Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~X.html)
[ISelectData::Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Y.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
