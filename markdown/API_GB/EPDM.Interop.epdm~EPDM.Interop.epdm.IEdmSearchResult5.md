---
title: "IEdmSearchResult5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearchResult5"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5.html"
---

# IEdmSearchResult5 Interface

Allows you to access a search result.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmSearchResult5
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmSearchResult5 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmSearchResult5 : public IEdmObject5
```

## Examples

[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

This interface:

- inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).
- is extended by [IEdmSearchResult6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6.html) which provides the ability to perform favorite searches and get accurate sizes of very large files.

To use this interface:

1. Obtain an object for this interface by calling [IEdmSearch5::GetFirstResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html) or [IEdmSearch10::GetFirstFavoriteResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10~GetFirstFavoriteResult.html).
2. Determine the type of the result object by calling one of the inherited properties on the IEdmSearchResult5 object, [ID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5~ID.html) or [Name](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5~Name.html).
3. If the type of this search result is a:

  1. file, cast this interface's object to [IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html).
  2. folder, cast this interface's object to [IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html).

## Accessors

IEdmSearch5::GetFirstResult

[IEdmSearch5::GetNextResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetNextResult.html)

IEdmSearch10::GetFirstFavoriteResult

## See Also

[IEdmSearchResult5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
