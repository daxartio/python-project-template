use pyo3::prelude::*;

/// Hello world function.
#[pyfunction]
fn hello() -> PyResult<String> {
    Ok("Hello, world!".to_string())
}

/// {{ cookiecutter.pkg_name }} package.
#[pymodule]
fn _{{ cookiecutter.pkg_name }}(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello, m)?)?;
    Ok(())
}
