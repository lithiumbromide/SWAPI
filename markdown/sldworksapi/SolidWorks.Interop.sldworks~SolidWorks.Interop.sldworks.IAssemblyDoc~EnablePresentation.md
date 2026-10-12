---
title: "EnablePresentation Property (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "EnablePresentation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnablePresentation.html"
---

# EnablePresentation Property (IAssemblyDoc)

Gets or sets whether the assembly is in presentation mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnablePresentation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

instance.EnablePresentation = value

value = instance.EnablePresentation
```

### C#

```csharp
System.bool EnablePresentation {get; set;}
```

### C++/CLI

```cpp
property System.bool EnablePresentation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables presentation mode, false disables it

## VBA Syntax

See [AssemblyDoc::EnablePresentation](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~EnablePresentation.html).

## Remarks

Call this property before calling [IComponent2::PresentationTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~PresentationTransform.html) because presentation transforms are effective only in this mode. This property prohibits reconfiguring the FeatureManager design tree when SOLIDWORKS is using the presentation transforms. This property also prohibits selections in the model view.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::GetTotalTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.html)
[IComponent2::RemovePresentationTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform.html)
[IComponent2::Transform2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
