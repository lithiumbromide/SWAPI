---
title: "ISafeArrayUtility Interface"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html"
---

# ISafeArrayUtility Interface

Access the ISafeArrayUtility interface, which can:

- get an unpacked array of native SOLIDWORKS Dispatch-based objects of the same data type and return a packed Variant SafeArray to use in methods that requires passing a packed Variant SafeArray.
- get a packed Variant SafeArray and return an unpacked array of native SOLIDWORKS Dispatch-based objects of the same data type.
- get a Variant SafeArray and return the number of SafeArray objects in the Variant SafeArray and their data type.
- get and put a value in a Variant SafeArray of the same data type.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISafeArrayUtility
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
```

### C#

```csharp
public interface ISafeArrayUtility
```

### C++/CLI

```cpp
public interface class ISafeArrayUtility
```

## Examples

[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)
[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)
[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)
[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)

## Remarks

The ISafeArrayUtility interface replaces the SOLIDWORKS SafeArray template class, which you might have used in earlier versions of SOLIDWORKS to instantiate SafeArrays for methods requiring Variant arrays in your C++ projects.

This ISafeArrayUtility interface's methods are only compatible with raw pointers and BSTRs; this interface's methods are not compatible with smart pointers (i.e., reference counted) or the Active Template Library (ATL) class CComBSTR. For example:

- - IDispatch* pDisp1; //This works

    IDispatchPtr pDisp2 //This does not work

    CComPtr<IDispatch> pDisp3 //This does not work

    BSTR fileName1 //This works

    CComBSTR fileName2 //This does not work

## Accessors

[ISldWorks::GetSafeArrayUtility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetSafeArrayUtility.html)

## Access Diagram

[SafeArrayUtility](SWObjectModel.pdf#SafeArrayUtility)

## See Also

[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
