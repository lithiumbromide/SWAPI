---
title: "GetNext Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.html"
---

# GetNext Method (IModelView)

Gets the next model view after this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Object

value = instance.GetNext()
```

### C#

```csharp
System.object GetNext()
```

### C++/CLI

```cpp
System.Object^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) or Nothing or null if no more model views exist

## VBA Syntax

See [ModelView::GetNext](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetNext.html).

## Examples

[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)

## Remarks

You can traverse through the model views in a document by using this method. When this method returns Nothing or null, you have reached the end of the list.

See [IModelDoc2::EnumModelViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EnumModelViews.html) for a method for traversing the model views on a document.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IEnumModelViews::Next Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Next.html)
[IModelDoc2::ActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.html)
[IModelDoc2::IActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)
[IModelView::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
