---
title: "IPartDoc Interface"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html"
---

# IPartDoc Interface

Provides access to functions that perform operations on parts in part documents.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPartDoc
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
```

### C#

```csharp
public interface IPartDoc
```

### C++/CLI

```cpp
public interface class IPartDoc
```

## VBA Syntax

See [PartDoc](ms-its:sldworksapivb6.chm::/sldworks~PartDoc.html).

## Examples

[Get Sketches (C++)](Get_Sketches_Example_CPlusPlus_COM.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Create Imported Surface Body From Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)
[Get Differences Between Parts (VBA)](Get_Differences_Between_Parts_Example_VB.htm)
[Import Step File (C#)](Import_STEP_File_Example_CSharp.htm)
[Import Step File (VB.NET)](Import_STEP_File_Example_VBNET.htm)
[Import Step File (VBA)](Import_STEP_File_Example_VB.htm)

## Remarks

This interface provides functions that allow you to:

- create bodies and features.
- perform suppress operations.
- obtain part extents and tessellation.
- locate entities by name.

The SOLIDWORKS API also has functions that are common to all document types. For example, determining the file name associated with a document would be a common operation. To expose common document-level functions, the SOLIDWORKS API uses the [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object.

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks_namespace.html) topic for a list of delegates for this interface.

## Accessors

[IBeltChainFeatureData::AccessBeltPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~AccessBeltPart.html)

## Access Diagram

[PartDoc](SWObjectModel.pdf#PartDoc)

## See Also

[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
