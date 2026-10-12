---
title: "DisplayTitle Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "DisplayTitle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~DisplayTitle.html"
---

# DisplayTitle Property (IComponent2)

Gets this component's title as displayed in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DisplayTitle As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.DisplayTitle
```

### C#

```csharp
System.string DisplayTitle {get;}
```

### C++/CLI

```cpp
property System.String^ DisplayTitle {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Display title

## VBA Syntax

See [Component2::DisplayTitle](ms-its:sldworksapivb6.chm::/sldworks~Component2~DisplayTitle.html).

## Remarks

To get or set the display title of an assembly, drawing or part, use [IModelDocExtension::DisplayTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayTitle.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2021 SP03, Revision Number 29.3
