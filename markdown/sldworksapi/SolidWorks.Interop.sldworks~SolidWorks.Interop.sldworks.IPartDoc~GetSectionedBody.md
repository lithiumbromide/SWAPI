---
title: "GetSectionedBody Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetSectionedBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetSectionedBody.html"
---

# GetSectionedBody Method (IPartDoc)

Gets the sectioned body seen in the specified drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSectionedBody( _
   ByVal ViewIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ViewIn As System.Object
Dim value As System.Object

value = instance.GetSectionedBody(ViewIn)
```

### C#

```csharp
System.object GetSectionedBody(
   System.object ViewIn
)
```

### C++/CLI

```cpp
System.Object^ GetSectionedBody(
   System.Object^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`: [Model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html)

### Return Value

[Sectioned body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PartDoc::GetSectionedBody](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetSectionedBody.html).

## Remarks

To determine if the desired model view is currently displaying a sectioned view, use [IModelView::GetDisplayState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetDisplayState.html).

If you need the full body representation, use [IPartDoc::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetBodies2.html) or [IPartDoc::EnumBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumBodies3.html), which ignores the sectioning operation.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::IGetSectionedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetSectionedBody2.html)
