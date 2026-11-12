---
title: "IncludeHiddenBodiesOrComponents Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "IncludeHiddenBodiesOrComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.html"
---

# IncludeHiddenBodiesOrComponents Property (IMassProperty2)

Gets or sets whether to include the mass properties of hidden bodies/components.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeHiddenBodiesOrComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Boolean

instance.IncludeHiddenBodiesOrComponents = value

value = instance.IncludeHiddenBodiesOrComponents
```

### C#

```csharp
System.bool IncludeHiddenBodiesOrComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeHiddenBodiesOrComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include the mass properties of hidden bodies/components, false to not

## VBA Syntax

See [MassProperty2::IncludeHiddenBodiesOrComponents](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~IncludeHiddenBodiesOrComponents.html).

## Remarks

After setting this property to true, be sure to call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.html) before using the IMassProperty2 properties.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)
[IMassProperty2::SelectedItems Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SelectedItems.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
