---
title: "DeleteStyle Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "DeleteStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.html"
---

# DeleteStyle Method (IAnnotation)

Deletes the specified style.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteStyle( _
   ByVal StyleName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim StyleName As System.String
Dim value As System.Boolean

value = instance.DeleteStyle(StyleName)
```

### C#

```csharp
System.bool DeleteStyle(
   System.string StyleName
)
```

### C++/CLI

```cpp
System.bool DeleteStyle(
   System.String^ StyleName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleName`: Name of the style to delete

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [Annotation::DeleteStyle](ms-its:sldworksapivb6.chm::/sldworks~Annotation~DeleteStyle.html).

## Remarks

The current styleis set to <NONE>. Dimensions and annotations retain the properties previously applied by the style unless the items are [reset to the document default](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::AddOrUpdateStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.html)
[IAnnotation::ApplyDefaultStyleAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.html)
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.html)
[IAnnotation::LoadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.html)
[IAnnotation::SaveStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.html)
[IAnnotation::SetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
