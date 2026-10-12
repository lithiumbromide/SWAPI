---
title: "AddOrUpdateStyle Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "AddOrUpdateStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.html"
---

# AddOrUpdateStyle Method (IAnnotation)

Adds or updates the annotation linked to the specified style.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddOrUpdateStyle( _
   ByVal StyleName As System.String, _
   ByVal BreakLinks As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim StyleName As System.String
Dim BreakLinks As System.Boolean
Dim value As System.Boolean

value = instance.AddOrUpdateStyle(StyleName, BreakLinks)
```

### C#

```csharp
System.bool AddOrUpdateStyle(
   System.string StyleName,
   System.bool BreakLinks
)
```

### C++/CLI

```cpp
System.bool AddOrUpdateStyle(
   System.String^ StyleName,
   System.bool BreakLinks
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleName`: Name of the style to add or update
- `BreakLinks`: True to break all links to this style, false to not

### Return Value

Ture if the operation succeeds, false if it fails

## VBA Syntax

See [Annotation::AddOrUpdateStyle](ms-its:sldworksapivb6.chm::/sldworks~Annotation~AddOrUpdateStyle.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::ApplyDefaultStyleAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.html)
[IAnnotation::DeleteStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.html)
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.html)
[IAnnotation::LoadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.html)
[IAnnotation::SaveStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.html)
[IAnnotation::SetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
