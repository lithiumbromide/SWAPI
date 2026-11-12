---
title: "ModelDoc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc.htm"
---

# ModelDoc

## ModelDoc Object

This object and its methods and properties are obsolete and have been superseded by [ModelDoc2](sldworksAPI.chm::/ModelDoc2/ModelDoc2.htm).

| image\sldworks.gif |
| --- |

|  | image\ModelDoc_h_shg.gif |
| --- | --- |

|  | image\branch2.gif image\Annotation.gif |
| --- | --- |
|  | image\branch2.gif image\Dimension.gif |
|  | image\branch2.gif image\Sketch.gif |
|  | image\branch2.gif image\ModelView.gif |
|  | image\branch2.gif image\DesignTable.gif |
|  | image\branch2.gif image\Attribute.gif |
|  | image\branch2.gif image\Configuration.gif |
|  | image\branch2.gif image\Feature.gif |
|  | image\branch2.gif image\FeatMgrView.gif |
|  | image\branch2.gif image\SelectionMgr.gif |
|  | image\branch2.gif image\LayerMgr.gif |
|  | image\branch1.gif image\Layer.gif |

In SolidWorks, there are three main document types: parts, drawings and assemblies. Each document type has its own API object (PartDoc, DrawingDoc and AssemblyDoc) with its own set of related functions. For example, the Assembly::AddComponent function exists on the AssemblyDoc object because adding components is specific to assembly documents.

The SolidWorks API also has functions that are common to all document types. For example, printing, saving or determining the file name associated with a document would be common operations. To expose common document-level functions, the SolidWorks API uses the ModelDoc object.

The ModelDoc object provides direct access to the PartDoc, DrawingDoc and AssemblyDoc Objects. This is important to recognize. For COM applications, it means the ModelDoc object can be obtained from any of these three objects using QueryInterface. Likewise, based on the type of document represented by the ModelDoc pointer, the related PartDoc, DrawingDoc or AssemblyDoc object can be obtained from the ModelDoc object also using QueryInterface. To determine which underlying interface is supported, you can use standard QueryInterface techniques, or you can use ModelDoc::GetType.

For OLE applications, this relationship means you can simply define a new IModelDoc object which uses the same dispatch pointer as your IPartDoc, IDrawingDoc, or IAssemblyDoc object. Likewise, given a part document, you can use its ModelDoc dispatch pointer to define a new PartDoc object. Before doing this, and before calling a function which is on one of the underlying objects, you should verify the document type using ModelDoc::GetType. If, for example, ModelDoc::GetType indicates that this ModelDoc object represents an assembly, then it is safe to use the dispatch pointer to define a new IAssemblyDoc object and to call any of the AssemblyDoc functions.

NOTE: Visual Basic applications will interpret the pointer for you automatically. This means you can simply use the given document object to call any ModelDoc function or, based on the document type, to call any of the PartDoc, DrawingDoc or AssemblyDoc functions.
