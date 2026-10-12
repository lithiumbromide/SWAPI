---
title: "ChangeProject Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "ChangeProject"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ChangeProject.html"
---

# ChangeProject Method (IPDMWDocument)

Moves the document to the specified project.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ChangeProject( _
   ByVal project As System.String, _
   ByVal bSelectedItem As System.Boolean, _
   ByVal i_childrenType As PDMWChildrenType, _
   ByVal bIgnoreLinks As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim project As System.String
Dim bSelectedItem As System.Boolean
Dim i_childrenType As PDMWChildrenType
Dim bIgnoreLinks As System.Boolean

instance.ChangeProject(project, bSelectedItem, i_childrenType, bIgnoreLinks)
```

### C#

```csharp
void ChangeProject(
   System.string project,
   System.bool bSelectedItem,
   PDMWChildrenType i_childrenType,
   System.bool bIgnoreLinks
)
```

### C++/CLI

```cpp
void ChangeProject(
   System.String^ project,
   System.bool bSelectedItem,
   PDMWChildrenType i_childrenType,
   System.bool bIgnoreLinks
)
```

### Parameters

- `project`: Project to which to move the document
- `bSelectedItem`: TRUE to move document, FALSE to not
- `i_childrenType`: Type of children documents, as defined in [PDMWChildrenType](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWChildrenType.html), to move to the new project
- `bIgnoreLinks`: TRUE to ignore any references from other projects to the document, FALSE to not

### Return Value

True to ignore any references from other projects to the document, false to not

## VBA Syntax

See [PDMWDocument::ChangeProject](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~ChangeProject.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 FCS
