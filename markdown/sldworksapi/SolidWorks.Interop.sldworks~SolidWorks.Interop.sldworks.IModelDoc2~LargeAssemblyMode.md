---
title: "LargeAssemblyMode Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "LargeAssemblyMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LargeAssemblyMode.html"
---

# LargeAssemblyMode Property (IModelDoc2)

Gets or sets Large Assembly Mode for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeAssemblyMode As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

instance.LargeAssemblyMode = value

value = instance.LargeAssemblyMode
```

### C#

```csharp
System.bool LargeAssemblyMode {get; set;}
```

### C++/CLI

```cpp
property System.bool LargeAssemblyMode {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables Large Assembly Mode, false disables it

## VBA Syntax

See [ModelDoc2::LargeAssemblyMode](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~LargeAssemblyMode.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
