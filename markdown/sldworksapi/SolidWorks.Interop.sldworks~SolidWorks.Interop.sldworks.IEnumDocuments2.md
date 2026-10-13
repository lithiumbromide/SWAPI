---
title: "IEnumDocuments2 Interface"
project: "SOLIDWORKS API Help"
interface: "IEnumDocuments2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.html"
---

# IEnumDocuments2 Interface

Allows access to a [documents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) enumeration.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IEnumDocuments2
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDocuments2
```

### C#

```csharp
public interface IEnumDocuments2
```

### C++/CLI

```cpp
public interface class IEnumDocuments2
```

## VBA Syntax

See [EnumDocuments2](ms-its:sldworksapivb6.chm::/sldworks~EnumDocuments2.html).

## Examples

[Get List of Open Documents (C++)](Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm)
[Traverse All Open Documents (C++)](Traverse_All_Open_Documents_Example_CPlusPlus_COM.htm)

## Remarks

For use in in-process DLLs only.

The list of [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) objects in the IEnumDocuments2 object contains all open IModelDoc2 pointers, including IModelDoc2 objects opened as file references (for example, from an assembly or drawing). You can use [IModelDoc2::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Visible.html) to determine if a particular document has its own window and is visible to the user.

## Accessors

[IEnumDocuments2::Clone](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDocuments2~Clone.html)

[ISldWorks::EnumDocuments2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~EnumDocuments2.html)

## Access Diagram

[EnumDocuments2](SWObjectModel.pdf#EnumDocuments2)

## See Also

[IEnumDocuments2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
