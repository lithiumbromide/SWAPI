---
title: "LoadStyle Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "LoadStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.html"
---

# LoadStyle Method (IAnnotation)

Loads the specified style.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadStyle( _
   ByVal PathName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim PathName As System.String
Dim value As System.Boolean

value = instance.LoadStyle(PathName)
```

### C#

```csharp
System.bool LoadStyle(
   System.string PathName
)
```

### C++/CLI

```cpp
System.bool LoadStyle(
   System.String^ PathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathName`: Path and filename of the style to load

### Return Value

Ture if the style is loaded, false if not

## VBA Syntax

See [Annotation::LoadStyle](ms-its:sldworksapivb6.chm::/sldworks~Annotation~LoadStyle.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::AddOrUpdateStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.html)
[IAnnotation::ApplyDefaultStyleAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.html)
[IAnnotation::DeleteStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.html)
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.html)
[IAnnotation::SaveStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.html)
[IAnnotation::SetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
