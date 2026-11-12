---
title: "Understanding the SOLIDWORKS API Class Hierarchy"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Understanding_the_SolidWorks_API_Class_Hierarchy.htm"
---

# Understanding the SOLIDWORKS API Class Hierarchy

SOLIDWORKS does not document its API with a complete class hierarchy diagram, much like the famous MFC and .NET/WinFX class hierarchy diagrams. The reason for this is that MFC and .NET rely heavily on:

- Classes
- Implementation inheritance
- Casting between classes using static casts (C++)

These types of class libraries and APIs can often benefit from a hierarchy diagram.

However, SOLIDWORKS is a COM-based API that uses:

- Interfaces
- Interface inheritance
- Factory methods to return interfaces on existing and new objects
- Casting between interfaces through:

  - QueryInterface (C++), which returns a pointer to a specified interface on an object to which a client currently holds an interface pointer.
  - direct assignment (VB/VB.NET).
  - the is/as reserved words (C#).

While a graphical hierarchy diagram often does not convey as much information in this style of API, there are a few places where it can be useful.

### Interface Inheritance in the SOLIDWORKS API

Objects that implement:

- [IAssemblyDoc](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAssemblyDoc.html), [IDrawingDoc](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDrawingDoc.html), or [IPartDoc](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPartDoc.html) can QueryInterface to [IModelDoc2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDoc2.html).
- [IEdge](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IEdge.html), [IFace2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFace2.html), [IFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature.html), [ILoop2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ILoop2.html), or [IVertex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IVertex.html) can QueryInterface to [IEntity](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IEntity.html).
- [IBomTableAnnotation](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBomTableAnnotation.html), [IHoleTableAnnotation](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IHoleTableAnnotation.html), [IRevisionTableAnnotation](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IRevisionTableAnnotation.html), [IWeldmentCutListAnnotation](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IWeldmentCutListAnnotation.html), and other table-annotation interfaces can QueryInterface to [ITableAnnotation](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ITableAnnotation.html). See [swTableAnnotationType_e](swconst.chm::/SolidWorks.interop.swconst~SolidWorks.interop.swconst.swTableAnnotationType_e.html) for a list of the interfaces that can QueryInterface to ITableAnnotation.
- [IAttribute](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAttribute.html) also can QueryInterface to [IFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature.html).
- [ISketchArc](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchArc.html), [ISketchEllipse](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchEllipse.html), [ISketchLine](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchLine.html), [ISketchParabola](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchParabola.html), [ISketchPoint](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchPoint.html), [ISketchSpline](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchSpline.html), or [ISketchText](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchText.html) can QueryInterface to [ISketchSegment](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchSegment.html).
- PropertyManager page controls, such as [IPropertyManagerPageActiveX](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageActiveX.html), [IPropertyManagerPageBitmap](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageBitmap.html), [IPropertyManagerPageBitmapButton](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageBitmapButton.html), [IPropertyManagerPageButton](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageButton.html), etc., can QueryInterface to [IPropertyManagerPageControl](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageControl.html).

NOTE: The phrase can QueryInterface to is synonymous with implements or can be assigned to in Visual Basic.

While it is technically incorrect to say, for example, that IPartDoc derives from IModelDoc2, the way that developers use these interfaces is similar to the way they would use a derived class with implementation inheritance.

### Using methods as an alternative to QueryInterface/Interface inheritance

There are several other areas of the API that use other methods to perform operations similar to a QueryInterface().

- [IAnnotation::GetSpecificAnnotation](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAnnotation~GetSpecificAnnotation.html) can return:
- [IFeature::GetSpecificFeature2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetSpecificFeature2.html) can return:

### Accessors

To find out how to get a specific SOLIDWORKS interface or object from other SOLIDWORKS interfaces or objects, use the Accessors link located at the bottom of an interface's topic.

### Reference material

For more information on classes, objects, casting, interfaces, QueryInterface, COM, and inheritance, see:

- Inside COM by Dale Rogerson. (Microsoft Press)
- Programming .NET Components by Juval Lowy (O'Reilly)
