---
title: "AutomaticViewUpdate Property (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AutomaticViewUpdate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutomaticViewUpdate.html"
---

# AutomaticViewUpdate Property (IDrawingDoc)

Gets or sets whether the drawing views in this drawing are automatically updated if the underlying model in that drawing view changes.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutomaticViewUpdate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Boolean

instance.AutomaticViewUpdate = value

value = instance.AutomaticViewUpdate
```

### C#

```csharp
System.bool AutomaticViewUpdate {get; set;}
```

### C++/CLI

```cpp
property System.bool AutomaticViewUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True updates the views automatically, false does not

## VBA Syntax

See [DrawingDoc::AutomaticViewUpdate](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AutomaticViewUpdate.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
