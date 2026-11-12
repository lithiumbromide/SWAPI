---
title: "XorHighlight Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "XorHighlight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~XorHighlight.html"
---

# XorHighlight Property (IModelView)

Gets or sets the Xor highlight state.

## Syntax

### Visual Basic (Declaration)

```vb
Property XorHighlight As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Boolean

instance.XorHighlight = value

value = instance.XorHighlight
```

### C#

```csharp
System.bool XorHighlight {get; set;}
```

### C++/CLI

```cpp
property System.bool XorHighlight {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to Xor the hightlight state, false to not

## VBA Syntax

See [ModelView::XorHighlight](ms-its:sldworksapivb6.chm::/sldworks~ModelView~XorHighlight.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
