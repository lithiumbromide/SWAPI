---
title: "EnumRelatedBodies Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "EnumRelatedBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumRelatedBodies.html"
---

# EnumRelatedBodies Method (IComponent2)

Creates an enumerated list of bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumRelatedBodies() As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As EnumBodies2

value = instance.EnumRelatedBodies()
```

### C#

```csharp
EnumBodies2 EnumRelatedBodies()
```

### C++/CLI

```cpp
EnumBodies2^ EnumRelatedBodies();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [enumerated list of bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [Component2::EnumRelatedBodies](ms-its:sldworksapivb6.chm::/sldworks~Component2~EnumRelatedBodies.html).

## Remarks

The list contains only those bodies associated with reference surfaces. You get a list of bodies that are related to the model, but the list does not include the part body itself.

A reference surface feature might consist of one or more surfaces sewn together. SOLIDWORKS represents each reference surface feature with two bodies: one to represent the front faces and one to represent the back faces. Each IBody2 object has one or more faces depending on whether the reference surface feature is a set of sewn surfaces or a single underlying surface. The corresponding faces for each body pair should have normal vectors that are opposite.

To use the enumerated list, see [IEnumBodies2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2~Next.html), [IEnumBodies2::Skip](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2~Skip.html), [IEnumBodies2::Reset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2~Reset.html), and [IEnumBodies2::Clone](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2~Clone.html).

If a component is suppressed or lightweight, this method might return NULL because the component has not been loaded into memory by SOLIDWORKS. For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
