---
title: "DisplayZebraStripes Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "DisplayZebraStripes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayZebraStripes.html"
---

# DisplayZebraStripes Property (IModelView)

Gets or sets the zebra-line display state.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayZebraStripes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Boolean

instance.DisplayZebraStripes = value

value = instance.DisplayZebraStripes
```

### C#

```csharp
System.bool DisplayZebraStripes {get; set;}
```

### C++/CLI

```cpp
property System.bool DisplayZebraStripes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the zebra stripes, false if not

## VBA Syntax

See [ModelView::DisplayZebraStripes](ms-its:sldworksapivb6.chm::/sldworks~ModelView~DisplayZebraStripes.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
