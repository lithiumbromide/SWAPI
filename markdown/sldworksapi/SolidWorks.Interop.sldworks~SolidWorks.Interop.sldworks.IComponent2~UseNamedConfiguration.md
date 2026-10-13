---
title: "UseNamedConfiguration Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "UseNamedConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~UseNamedConfiguration.html"
---

# UseNamedConfiguration Property (IComponent2)

Gets whether a specified configuration or the in-use/last active configuration is used.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UseNamedConfiguration As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.UseNamedConfiguration
```

### C#

```csharp
System.bool UseNamedConfiguration {get;}
```

### C++/CLI

```cpp
property System.bool UseNamedConfiguration {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if a configuration is specified and used, false if the in-use/last active configuration is used

## VBA Syntax

See [Component2::UseNamedConfiguration](ms-its:sldworksapivb6.chm::/sldworks~Component2~UseNamedConfiguration.html).

## Remarks

Use [IAssemblyDoc::CompConfigProperties4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.html) to set this property.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
