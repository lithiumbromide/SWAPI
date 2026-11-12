---
title: "ResolveOutOfDateLightWeightComponents Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ResolveOutOfDateLightWeightComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ResolveOutOfDateLightWeightComponents.html"
---

# ResolveOutOfDateLightWeightComponents Method (IDrawingDoc)

Resolves out-of-date lightweight components in the selected drawing view or drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function ResolveOutOfDateLightWeightComponents() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Boolean

value = instance.ResolveOutOfDateLightWeightComponents()
```

### C#

```csharp
System.bool ResolveOutOfDateLightWeightComponents()
```

### C++/CLI

```cpp
System.bool ResolveOutOfDateLightWeightComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if out-of-date lightweight components are resolved, false if not

## VBA Syntax

See [DrawingDoc::ResolveOutOfDateLightWeightComponents](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ResolveOutOfDateLightWeightComponents.html).

## Remarks

This method also resolves a selected out-of-date lightweight component and any out-of-date lightweight sub-components, in a drawing document.

You must select a drawing view, drawing sheet, or an out-of-date lightweight component before using this method.

| If... | Then... |
| --- | --- |
| Drawing view is selected | All out-of-date lightweight components in that drawing view are resolved |
| Drawing sheet is selected | All-out-of-date lightweight components in that drawing sheet are resolved |
| Out-of-date lightweight component is selected | It and any out-of-date lightweight sub-components are resolved |
| Your selection is invalid | This method returns false |

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.html)
[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IDrawingDoc::ChangeComponentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeComponentLayer.html)
[IDrawingDoc::OnComponentProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~OnComponentProperties.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
