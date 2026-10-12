---
title: "Direction Property (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Direction.html"
---

# Direction Property (IShellFeatureData)

Gets and sets the direction of this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Direction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim value As System.Integer

instance.Direction = value

value = instance.Direction
```

### C#

```csharp
System.int Direction {get; set;}
```

### C++/CLI

```cpp
property System.int Direction {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 for inward shell, 1 for outward shell

## VBA Syntax

See [ShellFeatureData::Direction](ms-its:sldworksapivb6.chm::/sldworks~ShellFeatureData~Direction.html).

## Examples

See the [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html) examples.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
