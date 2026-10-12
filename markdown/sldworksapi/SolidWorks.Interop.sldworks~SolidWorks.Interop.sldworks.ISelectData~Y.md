---
title: "Y Property (ISelectData)"
project: "SOLIDWORKS API Help"
interface: "ISelectData"
member: "Y"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Y.html"
---

# Y Property (ISelectData)

Gets or sets the Y coordinate for the selection point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Y As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectData
Dim value As System.Double

instance.Y = value

value = instance.Y
```

### C#

```csharp
System.double Y {get; set;}
```

### C++/CLI

```cpp
property System.double Y {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Y coordinate for the selection point

## VBA Syntax

See [SelectData::Y](ms-its:sldworksapivb6.chm::/sldworks~SelectData~Y.html).

## See Also

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html)
[ISelectData::X Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~X.html)
[ISelectData::Z Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Z.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
