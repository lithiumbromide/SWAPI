---
title: "X Property (ISelectData)"
project: "SOLIDWORKS API Help"
interface: "ISelectData"
member: "X"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~X.html"
---

# X Property (ISelectData)

Gets or sets the X coordinate for the selection point.

## Syntax

### Visual Basic (Declaration)

```vb
Property X As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectData
Dim value As System.Double

instance.X = value

value = instance.X
```

### C#

```csharp
System.double X {get; set;}
```

### C++/CLI

```cpp
property System.double X {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

X coordinate for the selection point

## VBA Syntax

See [SelectData::X](ms-its:sldworksapivb6.chm::/sldworks~SelectData~X.html).

## See Also

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html)
[ISelectData::Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Y.html)
[ISelectData::Z Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Z.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
