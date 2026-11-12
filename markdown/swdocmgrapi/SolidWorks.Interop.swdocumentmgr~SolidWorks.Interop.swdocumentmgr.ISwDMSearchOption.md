---
title: "ISwDMSearchOption Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSearchOption"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html"
---

# ISwDMSearchOption Interface

Allows you to specify the types of references and paths to search.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMSearchOption
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSearchOption
```

### C#

```csharp
public interface ISwDMSearchOption
```

### C++/CLI

```cpp
public interface class ISwDMSearchOption
```

## VBA Syntax

See [SwDMSearchOption](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSearchOption.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)

## Remarks

The search filters restrict the types of files returned. Any API that deals with file references needs a list of paths where it can search for files.

Every ISwDMSearchOption object is independent and is passed as a parameter. Because the DLL can be used by several applications at the same time; it cannot be global.

## Accessors

[ISwDMApplication::GetSearchOptionObject](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetSearchOptionObject.html)

[ISwDMExternalReferenceOption::SearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~SearchOption.html)

## See Also

[ISwDMSearchOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
