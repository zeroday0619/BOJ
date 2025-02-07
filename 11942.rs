use std::os::raw::{c_int, c_void};

extern "C" {
    fn write(fd: c_int, buf: *const c_void, count: usize) -> isize;
}

fn main() {
    let bytes: [u8; 15] = [
        234, 179, 160, 235, 160, 164, 
        235, 140, 128,               
        237, 149, 153,                
        234, 181, 144,                 
    ];

    unsafe {
        write(1, bytes.as_ptr() as *const c_void, bytes.len());
        write(1, b"\n".as_ptr() as *const c_void, 1);
    }
}